
#-----------------------------IMPORTS--------------------------------

from libqtile import layout

#-----------------------------LAYOUTS--------------------------------

def init_layouts():
	return [
		layout.MonadTall(
			border_focus = ("da4939"),
			border_normal = ("3f3f3f"),
			border_width = 4,
			ratio = 0.65,
			margin = 12),
		layout.Max()]

layouts = init_layouts()
