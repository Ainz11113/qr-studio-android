[app]
title = QR Studio
package.name = qrstudio
package.domain = org.qrstudio
source.dir = .
source.include_exts = py,png,jpg,html,css,js

version = 1.0

# Используем минимальный набор без C-зависимостей uvicorn
requirements = python3,kivy==2.3.0,fastapi,uvicorn,qrcode,pillow,pyjnius,android

orientation = portrait
fullscreen = 0

android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.skip_update = False