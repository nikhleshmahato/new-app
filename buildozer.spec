[app]

# (str) Title of your application
title = YourAppTitle

# (str) Package name
package.name = yourapp

# (str) Package domain (needed for a correct namespace)
package.domain = org.yourdomain

# (str) Source code encoding (default is utf-8)
source.include_exts = py,png,jpg,kv,atlas

# (list) Source files to include (let empty to include all the files)
source.include_patterns = *.py,*.kv

# (list) List of directories to exclude (default is empty)
source.exclude_dirs = tests, bin, venv

# (list) List of exclusions using pattern matching
source.exclude_exts = swp,pyc

# (str) Application versioning (default is 0.1)
version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,kivymd

# (str) Supported orientation (one of landscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not (default is 1)
fullscreen = 1

# (list) Permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE

[buildozer]

# (int) Log level (0 to 2)
log_level = 2

# (bool) Warn when running as root (0 to disable, 1 to enable)
warn_on_root = 1
