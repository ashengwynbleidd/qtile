# ----------Reference colors ----------

colors = {
    'black':   '#1a1816',
    'white':   '#f9f7f3',
    'red':     '#ff5640',
    'green':   '#d9ff80',
    'yellow':  '#ffc66d',
    'blue':    '#92d1ff',
    'magenta': '#c5c2ff',
    'cyan':    '#82ffe1',
    'grey1':   '#272822',
    'grey2':   '#3f3f3f',
}

# ---------- Layouts config ----------

# qtile documentaion for more information:
# http://docs.qtile.org/en/latest/manual/ref/layouts.html

layout_cfg = {
    'monadtall': {
        'border_normal': colors['grey1'],
        'border_focus':  colors['red'],
        'border_width':  3,
        'margin':        5,
    },
    'floating': {
        'border_normal': colors['grey2'],
        'border_focus':  colors['cyan'],
        'border_width':  3,
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
        'highlight_method':            'block',
        'block_highlight_text_color':  colors['black'],
        'other_current_screen_border': colors['grey2'],
        'this_current_screen_border':  colors['red'],
        'other_screen_border':         colors['grey2'],
        'this_screen_border':          colors['red'],
        'urgent_border':               colors['yellow'],
        'urgent_text':                 colors['red'],
        'foreground':                  colors['white'],
        'background':                  colors['black'],
        'inactive':                    colors['yellow'],
        'active':                      colors['red'],
        'rounded':                     False,
        'fontsize':                    22,
    },
    # ----------qtile prompt----------
    'prompt': {
        'record_history':      True,
        'ignore_dups_history': True,
        'max_history':         50,
        'cursor_color':        colors['red'],
        'foreground':          colors['red'],
        'background':          colors['black'],
        'fontsize':            14,
        'padding':             25,
    },
    # ----------battery percent----------
    'battery': {
        'format':          '{char} {percent:2.0%}',
        'low_foreground':  colors['red'],
        'foreground':      colors['black'],
        'background':      colors['yellow'],
        'discharge_char':  '',
        'charge_char':     '',
        'unknown_char':    '',
        'empty_char':      '',
        'full_char':       '',
        'show_short_text': False,
        'low_percentage':  0.25,
        'update_interval': 5,
        'fontsize':        14,
        'padding':         8,
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
        'foreground': colors['yellow'],
        'background': colors['black'],
        'fontsize':   12,
        'padding':    8,
    },
    # ----------layout display----------
    'layouticon': {
        'background': colors['grey2'],
        'padding':    10,
        'scale':      0.85,
    },
    # ------------------------------
    'blank': {'background': colors['black']},
}

# ---------- Screen config ----------

screen_cfg = {
    '1': {
        'opacity': 0.85,
        'size':    25
    },
    '2': {
        'opacity': 0.85,
        'size':    25
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
