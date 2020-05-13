
#-----------------------------IMPORTS--------------------------------

from libqtile.lazy import lazy

#---------------------------FUNCTIONS--------------------------------

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
