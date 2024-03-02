import os
import subprocess

import colors
from libqtile import hook, layout

import theme_setup
from desktop_rules import float_rules
from keys import key_shortcuts
from mouse_rules import init_mouse
from panel import panel_setup
from screen_rules import init_screens, init_widgets_screen1, init_widgets_screen2
from widgets_setup import init_widgets_list

keys = key_shortcuts()
groups = panel_setup(keys)

theme_setup.setup()
colors = theme_setup.special_colors

layout_theme = {
    "border_width": 2,
    "margin": 8,
    "border_focus": colors[1],
    "border_normal": colors[0],
}


layouts = [
    layout.MonadTall(**layout_theme),
    layout.VerticalTile(**layout_theme),
]

widget_defaults = dict(font="Ubuntu Bold", fontsize=12, padding=0, background=colors[0])

extension_defaults = widget_defaults.copy()

mouse = init_mouse()


if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = float_rules()
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser("~")
    subprocess.call([home + "/.config/qtile/autostart.sh"])


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits.
wmname = "LG3D"
