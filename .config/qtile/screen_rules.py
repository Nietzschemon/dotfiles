from libqtile import bar, hook, qtile
from libqtile.config import Screen

from widgets_setup import init_widgets_list


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1


# All other monitors' bars will display everything but widgets 22 (systray) and 23 (spacer).
def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    # del widgets_screen2[8:18]
    del widgets_screen2[9:]
    return widgets_screen2


# For adding transparency to your bar, add (background="#00000000") to the "Screen" line(s)
# For ex: Screen(top=bar.Bar(widgets=init_widgets_screen2(), background="#00000000", size=24)),
def init_screens(theme_colors=None):
    if theme_colors:
        return [
            Screen(
                top=bar.Bar(
                    widgets=init_widgets_screen1(), size=26, background=theme_colors[0]
                )
            ),
            Screen(
                top=bar.Bar(
                    widgets=init_widgets_screen2(), size=26, background=theme_colors[0]
                )
            ),
            Screen(
                top=bar.Bar(
                    widgets=init_widgets_screen2(), size=26, background=theme_colors[0]
                )
            ),
        ]
    else:
        return [
            Screen(top=bar.Bar(widgets=init_widgets_screen1(), size=26)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), size=26)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), size=26)),
        ]


def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)


def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)


def window_to_previous_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group)


def window_to_next_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group)


def switch_screens(qtile):
    i = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[i - 1].group
    qtile.current_screen.set_group(group)


@hook.subscribe.setgroup
def set_layout_on_screen_dimensions():
    for s in qtile.screens:
        if s.width > s.height:
            s.group.layout = "monadtall"
        else:
            s.group.layout = "verticaltile"
