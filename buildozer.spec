[app]
title = RemoteControlApp
package.name = remotecontrol
package.domain = org.kivy
source.dir = .
source.include_exts = py,kv
version = 1.0
requirements = python3,kivy,requests
orientation = portrait
fullscreen = 0

# Android specific
android.api = 33
android.minapi = 21
android.sdk = 24
android.ndk = 25b
android.build_tools = 34.0.0
android.accept_sdk_license = True

[buildozer]
log_level = 2
