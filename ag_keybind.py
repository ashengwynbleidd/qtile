from libqtile.config import Key, Group, Drag, Click
from libqtile.lazy import lazy
from ag_display import groups

# ---------- Keybindings ----------

keys = [
    # ----- Window manager options -----
    Key(['mod4', 'shift'], 'q', lazy.shutdown()),
    Key(['mod4', 'shift'], 'r', lazy.restart()),
    Key(['mod1'], 'q', lazy.window.kill()),
    # ----- Window toggle options -----
    Key(['mod1'], 'n', lazy.window.toggle_fullscreen()),
    Key(['mod1'], 'm', lazy.window.toggle_minimize()),
    Key(['mod1'], 'f', lazy.window.toggle_floating()),
    # ----- Changing focused window -----
    Key(['mod1'], 'Tab', lazy.layout.next()),
    Key(['mod1', 'control'], 'Up', lazy.layout.up()),
    Key(['mod1', 'control'], 'Down', lazy.layout.down()),
    # ----- Resizing & Rearranging layout window -----
    Key(['mod1', 'shift'], 'Up', lazy.layout.shuffle_up()),
    Key(['mod1', 'shift'], 'Down', lazy.layout.shuffle_down()),
    Key(['mod1'], 'Right', lazy.layout.grow_main()),
    Key(['mod1'], 'Left', lazy.layout.shrink_main()),
    Key(['mod1'], 'Up', lazy.layout.grow()),
    Key(['mod1'], 'Down', lazy.layout.shrink()),
    Key(['mod4'], 'space', lazy.layout.flip()),
    # ----- Spawning Applications -----
    Key(['mod4', 'shift'], 'Return', lazy.spawncmd()),
    Key(['mod4'], 'Return', lazy.spawn('alacritty')),
]

mouse = [
    # ----- Moving floating window -----
    Drag(['mod4'], 'Button1', lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    # ----- Resizing floating window -----
    Drag(['mod4'], 'Button3', lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    # ----- Bringing on top floating window -----
    Click(['mod4'], 'Button2', lazy.window.bring_to_front())]

for index in groups:
    keys.extend([
        # ----- Moving window to group[index] -----
        Key(['mod1', 'shift'], index.name, lazy.window.togroup(index.name)),
        # ----- Displaying group[index] -----
        Key(['mod1'], index.name, lazy.group[index.name].toscreen()),
        # ----- Displaying group[index-1] -----
        Key(['mod4', 'shift'], 'Tab', lazy.screen.prev_group()),
        # ----- Displaying group[index+1] -----
        Key(['mod4'], 'Tab', lazy.screen.next_group())])
