import io
import os
import sys
import threading
import qrcode
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, StreamingResponse

# Kivy импорты
from kivy.app import App
from kivy.clock import Clock
from kivy.utils import platform

app = FastAPI()


# --- Вспомогательная функция путей ---
def get_resource_path(relative_path: str) -> str:
  if hasattr(sys, '_MEIPASS'):
    return os.path.join(sys._MEIPASS, relative_path)
  return os.path.join(os.path.abspath('.'), relative_path)


# --- Эндпоинты FastAPI ---
@app.get('/', response_class=HTMLResponse)
def read_root():
  html_path = get_resource_path('index.html')
  if not os.path.exists(html_path):
    raise HTTPException(status_code=500, detail='index.html not found')
  with open(html_path, 'r', encoding='utf-8') as f:
    return f.read()


@app.get('/generate')
def generate(data: str):
  if not data:
    raise HTTPException(status_code=400, detail='No data provided')
  img = qrcode.make(data)
  buf = io.BytesIO()
  img.save(buf, format='PNG')
  buf.seek(0)
  return StreamingResponse(buf, media_type='image/png')


def start_server():
  import uvicorn

  uvicorn.run(app, host='127.0.0.1', port=18888, log_level='error')


# --- Нативный WebView под Android через PyJNIus ---
class QRMobileApp(App):

  def build(self):
    # 1. Запускаем локальный сервер
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()

    # 2. Если запускаемся на реальном Android устройства
    if platform == 'android':
      from android.runnable import run_on_ui_thread
      from jnius import autoclass

      Activity = autoclass('org.kivy.android.PythonActivity').mActivity
      WebView = autoclass('android.webkit.WebView')
      WebViewClient = autoclass('android.webkit.WebViewClient')

      @run_on_ui_thread
      def create_webview():
        webview = WebView(Activity)
        webview.getSettings().setJavaScriptEnabled(True)
        webview.setWebViewClient(WebViewClient())
        webview.loadUrl('http://127.0.0.1:18888')
        Activity.setContentView(webview)

      Clock.schedule_once(lambda dt: create_webview(), 0.5)

    return super().build()


if __name__ == '__main__':
  QRMobileApp().run()