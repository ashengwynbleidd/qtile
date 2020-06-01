# ----------Reference colors ----------

# colorsceme_1: #2b2b2b #3f3f3f #f9f7f3 #da4939 #a5c261 #ffc66d #6d9cbe #b6b3eb #519f8c

# colorsceme_2: #272822 #75715e #f8f8f2 #f92672 #a6e22e #f4bf75 #66d9ef #ae81ff #a1efe4

# ---------- Layouts config ----------

# qtile documentaion for more information:
# http://docs.qtile.org/en/latest/manual/ref/layouts.html

layout_cfg = {
    'monadtall': {
        'border_normal': '#2b2b2b',
        'border_focus': '#da4939',
        'border_width': 3,
        'margin': 5,
    },
    'floating': {
        'border_normal': '#2b2b2b',
        'border_focus': '#519f8c',
        'border_width': 3,
    }
}

# ---------- Group config ----------

# qtile documentaion for more information:
# http://docs.qtile.org/en/latest/manual/ref/commands.html#group

group_cfg = {
    '1': {
        # 'matches': ['Alacritty', 'xterm', 'urxvt'],
        'name': '1',
        'label': '    ',
        'layout': 'monadtall', },
    '2': {
        # 'matches': ['firefox', 'Midori'],
        'name': '2',
        'label': '    ',
        'layout': 'monadtall', },
    '3': {
        # 'matches': ['Code', 'Atom'],
        'name': '3',
        'label': '    ',
        'layout': 'monadtall', },
    '4': {
        # 'matches': None,
        'name': '4',
        'label': '    ',
        'layout': 'monadtall', },
    '5': {
        # 'matches': ['Steam', 'Wine'],
        'name': '5',
        'label': '    ',
        'layout': 'monadtall', },
    '6': {
        # 'matches': None,
        'name': '6',
        'label': '    ',
        'layout': 'monadtall', },
    '7': {
        # 'matches': None,
        'name': '7',
        'label': '    ',
        'layout': 'monadtall', },
    '8': {
        # 'matches': ['Thunar', 'Pcmanfm'],
        'name': '8',
        'label': '    ',
        'layout': 'monadtall', },
}

# ---------- Widget config ----------

# qtile documentaion for more information:
# http://docs.qtile.org/en/latest/manual/ref/widgets.html

widget_conf = {
    # ----------group display----------
    'groupbox': {
        'highlight_method': 'block',
        'block_highlight_text_color': '#2b2b2b',
        'other_current_screen_border': '#3f3f3f',
        'this_current_screen_border': '#da4939',
        'other_screen_border': '#3f3f3f',
        'this_screen_border': '#da4939',
        'urgent_border': '#ffc66d',
        'urgent_text': '#da4939',
        'foreground': '#f9f7f3',
        'background': '#2b2b2b',
        'inactive': '#ffc66d',
        'active': '#da4939',
        'rounded': False,
        'fontsize': 22,
    },
    # ----------qtile prompt----------
    'prompt': {
        'record_history': True,
        'ignore_dups_history': True,
        'max_history': 50,
        'cursor_color': '#da4939',
        'foreground': '#da4939',
        'background': '#2b2b2b',
        'fontsize': 14,
        'padding': 25,
    },
    # ----------battery percent----------
    'battery': {
        'format': '{char} {percent:2.0%}',
        'low_foreground': '#da4939',
        'foreground': '#2b2b2b',
        'background': '#ffc66d',
        'discharge_char': '',
        'charge_char': '',
        'unknown_char': '',
        'empty_char': '',
        'full_char': '',
        'show_short_text': False,
        'low_percentage': 0.25,
        'update_interval': 5,
        'fontsize': 15,
        'padding': 10,
    },
    # ----------clock & time----------
    'clock': {
        'format': ' %I:%M %p',
        'update_interval': 1
    },
    # ----------memory utilized----------
    'memory': {
        'format': ' {MemUsed} MiB',
        'update_interval': 5
    },
    # ----------cpu frequency----------
    'cpu': {
        'format': ' {freq_current} GHz',
        'update_interval': 5
    },
    # ----------text decoration----------
    'infotext': {
        'foreground': '#ffc66d',
        'background': '#3f3f3f',
        'fontsize': 12,
        'padding': 8,
    },
    # ----------layout display----------
    'layouticon': {
        'background': '#519f8c',
        'padding': 10,
        'scale': 0.85,
    },
    # ------------------------------
    'blank': {'background': '#2b2b2b'},
}

# ---------- Screen config ----------

screen_cfg = {
    '1': {
        'opacity': 0.8,
        'size': 25
    },
    '2': {
        'opacity': 0.8,
        'size': 25
    },
}

# ---------- Floating config ----------

floating_cfg = {
    'float_rule': [
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
        {'wmclass': 'ssh-askpass'},
    ]
}
