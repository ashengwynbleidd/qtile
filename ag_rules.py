
#-----------------------------IMPORTS--------------------------------

from libqtile import layout

#------------------------------RULES---------------------------------

def init_floating_layout():
	return layout.Floating(float_rules=[
		{'wmclass': 'confirm'},
		{'wmclass': 'dialog'},
		{'wmclass': 'download'},
		{'wmclass': 'error'},
		{'wmclass': 'file_progress'},
		{'wmclass': 'notification'},
		{'wmclass': 'splash'},
		{'wmclass': 'toolbar'},
		{'wmclass': 'confirmreset'},
		{'wmclass': 'makebranch'},
		{'wmclass': 'maketag'},
		{'wname': 'branchdialog'},
		{'wname': 'pinentry'},
		{'wmclass': 'ssh-askpass'}])

floating_layout = init_floating_layout()
