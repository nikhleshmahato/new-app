[app]
# (str) Title of your application
title = nikku

# (str) Package name
package.name = nikku

# (str) Package domain
package.domain = org.nikku

# (str) Source code encoding
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
requirements = python3,kivy,kivymd

# (str) Supported orientations
orientation = portrait

# (bool) Whether to use the fullscreen mode
fullscreen = 1

# (list) Permissions required by the app
android.permissions = INTERNET,ACCESS_NETWORK_STATE

# (str) Presplash of the application
presplash.filename = %(source.dir)s/images/presplash.png

# (str) Icon of the application
icon.filename = %(source.dir)s/images/icon.png

[buildozer]
# (int) Log level (0 to 2)
log_level = 2
warn_on_root = 1
