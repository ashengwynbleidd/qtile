
#-----------------------------IMPORTS--------------------------------

from libqtile.config import Key, Group, Drag, Click
from libqtile.lazy import lazy
from ag_groups import groups
from ag_functions import *

#----------------------------KEYBINDINGS------------------------------

sup = "mod4"
alt = "mod1"
shift = "shift"
ctrl = "control"
lmb = "Button1"
mmb = "Button2"
rmb = "Button3"

def init_keys():
	return [
		# ALT BINDINGS
		Key([alt], "q", lazy.window.kill()),
		Key([alt], "Tab", lazy.layout.next()),
		Key([alt], "n", lazy.window.toggle_fullscreen()),
		Key([alt], "m", lazy.window.toggle_minimize()),
		Key([alt], "f", lazy.window.toggle_floating()),
		# FOCUSING
		Key([alt, ctrl], "Up", lazy.layout.up()),
		Key([alt, ctrl], "Down", lazy.layout.down()),
		# SHUFFLING
		Key([alt, shift], "Up", lazy.layout.shuffle_up()),
		Key([alt, shift], "Down", lazy.layout.shuffle_down()),
		# RESIZING
		Key([alt], "Up", lazy.layout.grow()),
		Key([alt], "Down", lazy.layout.shrink()),
		Key([alt], "Right", lazy.layout.grow_main()),
		Key([alt], "Left", lazy.layout.shrink_main()),
		# FLIPPING
		Key([sup], "space", lazy.layout.flip()),
		# SPAWNING
		Key([sup, shift], "Return", lazy.spawncmd()),
		Key([sup], "Return", lazy.spawn("alacritty")),
		Key([sup], "b", lazy.spawn("firefox")),
		Key([sup], "c", lazy.spawn("atom")),
		# WINDOW MANAGER
		Key([sup, shift], "q", lazy.shutdown()),
		Key([sup, shift], "r", lazy.restart())]

keys = init_keys()

def init_mouse():
	return [
		Drag([sup], lmb, lazy.window.set_position_floating(), start=lazy.window.get_position()),
		Drag([sup], rmb, lazy.window.set_size_floating(), start=lazy.window.get_size()),
		Click([sup], mmb, lazy.window.bring_to_front())]

mouse = init_mouse()

for i in groups:
	keys.extend([
	Key([alt, shift], i.name, lazy.window.togroup(i.name), lazy.group[i.name].toscreen()),
	Key([alt], i.name, lazy.group[i.name].toscreen()),
	Key([sup, shift], "Tab", lazy.screen.prev_group()),
	Key([sup], "Tab", lazy.screen.next_group())])
