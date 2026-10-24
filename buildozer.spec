[app]

# (str) Title of your application
title = Musicphone

# (str) Package name
package.name = musicphone

# (str) Package domain (needed for android packaging)
package.domain = org.musicphone

# (list) Source files to include (let it empty to include all files)
source.include_exts = py,png,jpg,kv,atlas,mp3,wav,json

# (list) Source files to exclude (let it empty to exclude all files)
source.exclude_exts = spec

# (list) List of directory to exclude (let it empty to exclude all files)
source.exclude_dirs = bin, venv, .git, .github

# (str) Directory where the source files are located
source.dir = .

# (str) Application main file name
source.main = Musicphone.py

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# (int) Number of Android API to use as target by default
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use --private data storage (True) or --dir storage (False)
android.private_storage = True

# (list) Target architecture, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a, armeabi-v7a

# (bool) Enable AndroidX support
android.androidx = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_root = 1
