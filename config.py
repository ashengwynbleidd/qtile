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
#-----------------------------IMPORTS--------------------------------

import os
import re
import socket
import subprocess
from libqtile import hook
from ag_themes import colors
from ag_rules import floating_layout
from ag_layouts import layouts
from ag_screens import screens
from ag_groups import groups
from ag_keybinds import keys, mouse

#--------------------------STARTUP SCRIPT----------------------------

@hook.subscribe.startup_once
def startup_once():
		home = os.path.expanduser("~")
		subprocess.call([home + "/.config/qtile/fstart.sh"])

#-------------------------------------------------------------------

wmname = "Qtile"
focus_on_window_activation = "smart"
dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
auto_fullscreen = True
cursor_warp = False
main = None
