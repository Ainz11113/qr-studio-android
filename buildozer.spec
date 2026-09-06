[app]
title = QR Studio
package.name = qrstudio
package.domain = org.qrstudio
source.dir = .
source.include_exts = py,png,jpg,html,css,js

version = 1.0
requirements = python3,kivy,fastapi,uvicorn,qrcode,pillow,pyjnius,android

orientation = portrait
fullscreen = 0

android.permissions = INTERNET
android.api = 33
android.minapi = 21