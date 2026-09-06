[app]
title = QR Studio
package.name = qrstudio
package.domain = org.qrstudio
source.dir = .
source.include_exts = py,png,jpg,html,css,js

version = 1.0

# Основные зависимости Python
requirements = python3,kivy,fastapi,uvicorn,qrcode,pillow,pyjnius,android

orientation = portrait
fullscreen = 0

# Права и версии Android API
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True