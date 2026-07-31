[app]

title = SmartAI
package.name = smartai
package.domain = org.smartai

source.dir = .
source.include_exts = py,kv,png,jpg,jpeg,json,ttf

version = 1.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0

# Entry point
entrypoint = main.py

# Assets
icon.filename = assets/icon.png
presplash.filename = assets/splash.png

#
# Android Configuration
#

android.api = 33
android.minapi = 24
android.ndk = 25b

android.accept_sdk_license = True

android.archs = arm64-v8a, armeabi-v7a

android.permissions = INTERNET

#
# Logging
#

log_level = 2
warn_on_root = 1

#
# Build options
#

android.release_artifact = apk
