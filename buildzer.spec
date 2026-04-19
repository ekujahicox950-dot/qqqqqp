[app]

title = ControlPanel
package.name = controlpanel
package.domain = org.control

source.dir = .
source.include_exts = py,png,jpg,kv

version = 1.0

requirements = python3,kivy,kivymd,requests

orientation = portrait
fullscreen = 0

android.permissions = INTERNET

[buildozer]

log_level = 2
warn_on_root = 1
