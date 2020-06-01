from libqtile.config import Group, Screen
#from libqtile.config import Match
from libqtile import bar, widget, layout
from ag_confdata import layout_cfg, group_cfg
from ag_confdata import widget_conf, screen_cfg
from ag_confdata import floating_cfg

# ---------- Layouts & Groups ----------

layouts = [
    layout.MonadTall(**layout_cfg['monadtall']),
    layout.Floating(**layout_cfg['floating']),
    layout.Max()]

groups = []
for index in range(len(group_cfg)):
    groups.append(Group(**group_cfg[str(index+1)]))

# ---------- Widgets & Screens ----------

widget_defaults = dict(font='Roboto', fontsize=18)
extension_defaults = widget_defaults.copy()

widgets_list = [
    widget.CurrentLayoutIcon(**widget_conf['layouticon']),
    widget.GroupBox(**widget_conf['groupbox']),
    widget.Prompt(**widget_conf['prompt']),
    widget.Spacer(**widget_conf['blank']),
    widget.Memory(**widget_conf['memory'], **widget_conf['infotext']),
    widget.CPU(**widget_conf['cpu'], **widget_conf['infotext']),
    widget.Clock(**widget_conf['clock'], **widget_conf['infotext']),
    widget.Battery(**widget_conf['battery'])]

screens = []
for index in range(len(screen_cfg)):
    screens.append(Screen(top=bar.Bar(
        widgets=widgets_list, **screen_cfg[str(index+1)])))

# ---------- Floating rules ----------

floating_layout = layout.Floating(**floating_cfg)
