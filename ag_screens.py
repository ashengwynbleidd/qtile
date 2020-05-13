
#-----------------------------IMPORTS--------------------------------

from libqtile.config import Screen
from libqtile import bar
from ag_widgets import widgets_list

#-----------------------------SCREENS--------------------------------

def init_widgets_screen():
    return widgets_list

def init_screens():
    return [
    Screen(top=bar.Bar(
        widgets = init_widgets_screen(),
        opacity = 0.8,
        size = 30))]

screens = init_screens()
