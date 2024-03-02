import subprocess

from libqtile import qtile

# Make sure 'qtile-extras' is installed or this config will not work.
from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration

import colors

colors = colors.DoomOne
myTerm = "st"  # My terminal of choice


def init_widgets_list():
    widgets_list = [
        widget.Spacer(length=8),
        widget.TextBox(
            text=" ",
            font="JetBrainsMonoNerdFont",
            foreground=colors[1],
            padding=1,
            fontsize=24,
        ),
        widget.Prompt(font="JetBrainsMonoNerdFont", fontsize=14, foreground=colors[1]),
        widget.GroupBox(
            fontsize=11,
            margin_y=5,
            margin_x=5,
            padding_y=0,
            padding_x=1,
            borderwidth=3,
            active=colors[8],
            inactive=colors[1],
            rounded=False,
            highlight_color=colors[2],
            highlight_method="line",
            this_current_screen_border=colors[7],
            this_screen_border=colors[4],
            other_current_screen_border=colors[7],
            other_screen_border=colors[4],
        ),
        widget.TextBox(
            text="|",
            font="JetBrainsMonoNerdFont",
            foreground=colors[1],
            padding=2,
            fontsize=14,
        ),
        widget.CurrentLayoutIcon(
            # custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
            foreground=colors[1],
            padding=4,
            scale=0.6,
        ),
        widget.CurrentLayout(foreground=colors[1], padding=5),
        widget.TextBox(
            text="|",
            font="JetBrainsMonoNerdFont",
            foreground=colors[1],
            padding=2,
            fontsize=14,
        ),
        widget.WindowName(foreground=colors[6], max_chars=40),
        widget.Notify(
            forground=colors[1],
            fmt="  {} ",
            font="JetBrainsMonoNerdFont",
            fontsize=14,
            padding=8,
            default_timeout=30,
            default_low=30,
            default_urgent=360,
            decorations=[
                BorderDecoration(
                    colour=colors[2],
                    border_width=[0, 0, 2, 0],
                )
            ],
        ),
        widget.Systray(padding=3),
        widget.GenPollText(
            update_interval=0.2,
            func=lambda: subprocess.check_output(
                "echo -n 'Richard sucks'", shell=True, text=True
            ),
            foreground=colors[3],
            fmt="❤ {} ❤",
            decorations=[
                BorderDecoration(
                    colour=colors[3],
                    border_width=[0, 0, 2, 0],
                )
            ],
        ),
        widget.Spacer(length=8),
        widget.CPU(
            format="▓  Cpu: {load_percent}%",
            foreground=colors[4],
            decorations=[
                BorderDecoration(
                    colour=colors[4],
                    border_width=[0, 0, 2, 0],
                )
            ],
        ),
        widget.Spacer(length=8),
        widget.Memory(
            foreground=colors[8],
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(myTerm + " -e htop")},
            format="{MemUsed: .0f}{mm}",
            fmt="🖥  Mem: {} used",
            decorations=[
                BorderDecoration(
                    colour=colors[8],
                    border_width=[0, 0, 2, 0],
                )
            ],
        ),
        widget.Spacer(length=8),
        widget.DF(
            update_interval=60,
            foreground=colors[5],
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(myTerm + " -e df")},
            partition="/",
            # format = '[{p}] {uf}{m} ({r:.0f}%)',
            format="{uf}{m} free",
            fmt="🖴  Disk: {}",
            visible_on_warn=False,
            decorations=[
                BorderDecoration(
                    colour=colors[5],
                    border_width=[0, 0, 2, 0],
                )
            ],
        ),
        widget.Spacer(length=8),
        widget.Volume(
            foreground=colors[7],
            fmt="🕫  Vol: {}",
            decorations=[
                BorderDecoration(
                    colour=colors[7],
                    border_width=[0, 0, 2, 0],
                )
            ],
        ),
        widget.Spacer(length=8),
        widget.Clock(
            foreground=colors[8],
            format="⏱  %a, %b %d - %H:%M:%S",
            decorations=[
                BorderDecoration(
                    colour=colors[8],
                    border_width=[0, 0, 2, 0],
                )
            ],
        ),
        widget.Spacer(length=8),
    ]
    return widgets_list
