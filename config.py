#		+-------------------------------------------------+
#		|  ▄▄▄        ▄████  █     █░▓██   ██▓ ███▄    █  |
#		| ▒████▄     ██▒ ▀█▒▓█░ █ ░█░ ▒██  ██▒ ██ ▀█   █  |
#		| ▒██  ▀█▄  ▒██░▄▄▄░▒█░ █ ░█   ▒██ ██░▓██  ▀█ ██▒ |
#		| ░██▄▄▄▄██ ░▓█  ██▓░█░ █ ░█   ░ ▐██▓░▓██▒  ▐▌██▒ |
#		|  ▓█   ▓██▒░▒▓███▀▒░░██▒██▓   ░ ██▒▓░▒██░   ▓██░ |
#		|  ▒▒   ▓▒█░ ░▒   ▒ ░ ▓░▒ ▒     ██▒▒▒ ░ ▒░   ▒ ▒  |
#		|   ▒   ▒▒ ░  ░   ░   ▒ ░ ░   ▓██ ░▒░ ░ ░░   ░ ▒░ |
#		|   ░   ▒   ░ ░   ░   ░   ░   ▒ ▒ ░░     ░   ░ ░  |
#		|       ░  ░      ░     ░     ░ ░              ░  |
#		|                             ░ ░                 |
#		+-------------------------------------------------+

import os
import re
import socket
import subprocess
from libqtile import hook
from libqtile.lazy import lazy
from ag_display import layouts, groups
from ag_display import floating_layout
from ag_display import screens
from ag_keybind import keys, mouse

# ---------- Startup script ----------


@hook.subscribe.startup_once
def startup_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/fstart.sh'])

# ---------- Custom functions ----------


@lazy.function
def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i+1].name)


@lazy.function
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i-1].name)


@lazy.function
def window_to_next_screen():
    if qtile.currentWindow is not None:
        i = qtile.init_screens.index(qtile.currentScreen)
        qtile.currentWindow.togroup(qtile.screens[i+1].group.name)


@lazy.function
def window_to_prev_screen():
    if qtile.currentWindow is not None:
        i = qtile.init_screens.index(qtile.currentScreen)
        qtile.currentWindow.togroup(qtile.screens[i-1].group.name)

# --------------------------------------


wmname = 'Qtile'
focus_on_window_activation = 'smart'
dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
auto_fullscreen = True
cursor_warp = False
main = None
