[app]
title = QR Studio
package.name = qrstudio
package.domain = org.qrstudio
source.dir = .
source.include_exts = py,png,jpg,html,css,js

version = 1.0

# 1. Меняем pillow на pillow_python и добавляем android/pyjnius
requirements = python3,kivy==2.3.0,fastapi,uvicorn,qrcode,pillow_python,pyjnius,android

orientation = portrait
fullscreen = 0

# 2. Права и автоматическое согласие с лицензиями
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.skip_update = False