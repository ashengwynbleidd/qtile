
#-----------------------------IMPORTS--------------------------------

from libqtile import widget
from ag_themes import colors

#-----------------------------WIDGETS--------------------------------

widget_defaults = dict(font = 'sans', fontsize = 18, padding = 5)
extension_defaults = widget_defaults.copy()

def init_widgets_list():
	return [
		widget.Sep(
			foreground = colors[2],
			background = colors[0],
			linewidth = 0,
			padding = 12),
#----------------------------------------------------------------------
		widget.GroupBox(
			highlight_method = "block",
			block_highlight_text_color = colors [0],
			this_current_screen_border = colors[3],
			urgent_border = colors[5],
			foreground = colors[2],
			background = colors[0],
			inactive = colors[5],
			active = colors[3],
			rounded = False,
			fontsize = 40,
			spacing = 15,
			padding = 5),
#-----------------------------------------------------------------------
		widget.Sep(
			foreground = colors[2],
			background = colors[0],
			linewidth = 0,
			padding = 15),
#-----------------------------------------------------------------------
		widget.Prompt(
			background = colors[3],
			foreground = colors[0],
			fontsize = 15),
#-----------------------------------------------------------------------
		widget.WindowName(
			ignore_dups_history = True,
			cursor_color = colors[0],
			foreground = colors[2],
			background = colors[0],
			cursor = True,
			fontsize = 13),
#-----------------------------------------------------------------------
		widget.Systray(
			background = colors[0]),
#-----------------------------------------------------------------------
		widget.TextBox(
			foreground = colors[5],
			background = colors[0],
			fontsize = 30,
			padding = 5,
			text = ""),
#-----------------------------------------------------------------------
		widget.Clock(
			foreground = colors[2],
			background = colors[0],
			format = "%I:%M %p",
			fontsize = 13),
#-----------------------------------------------------------------------
		widget.Sep(
			foreground = colors[2],
			background = colors[0],
			linewidth = 0,
			padding = 15),
#-----------------------------------------------------------------------
		widget.CurrentLayoutIcon(
			background = colors[8],
			padding = 10,
			scale=0.85)]

widgets_list = init_widgets_list()
