import os

from libqtile.config import Key
from libqtile.lazy import lazy


# A function for hide/show all the windows in a group
@lazy.function
def minimize_all(qtile):
    for win in qtile.current_group.windows:
        if hasattr(win, "toggle_minimize"):
            win.toggle_minimize()


# A function for toggling between MAX and MONADTALL layouts
@lazy.function
def maximize_by_switching_layout(qtile):
    current_layout_name = qtile.current_group.layout.name
    if current_layout_name == "monadtall":
        qtile.current_group.layout = "max"
    elif current_layout_name == "max":
        qtile.current_group.layout = "monadtall"


def key_shortcuts():
    mod = "mod4"  # Sets mod key to SUPER/WINDOWS
    alt = "mod1"
    myTerm = "st"  # My terminal of choice
    myBrowser = "chromium"  # My browser of choice
    home = os.path.expanduser("~")
    return [
        # The essentials
        Key([mod], "Return", lazy.spawn(myTerm), desc="Terminal"),
        Key(
            [mod, "shift"],
            "Return",
            lazy.spawn("dmenu_run -fn Monospace-22"),
            desc="start dmenu",
        ),
        Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
        Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
        Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
        Key(
            [mod, "shift"],
            "c",
            lazy.spawn("st -e nvim " + home + "/.config/qtile/config.py"),
            desc="Open the config",
        ),
        # Key([mod, "shift"], "q", lazy.spawn("dm-logout -r"), desc="Logout menu"),
        # Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
        Key(
            [mod, "control", "shift"], "s", lazy.spawn("shutdown now"), desc="shutdown"
        ),
        Key([mod, "control", "shift"], "r", lazy.spawn("reboot"), desc="reboot"),
        Key(
            [mod, "control", "shift"],
            "l",
            lazy.spawn("xscreensaver-command -lock"),
            desc="lock computer",
        ),
        # Website
        Key([mod], "w", lazy.spawn(myBrowser), desc="Chromium"),
        Key(
            [mod, "shift"],
            "w",
            lazy.spawn("chromium --incognito"),
            desc="chromium incognito",
        ),
        Key([mod, alt], "w", lazy.spawn("brave --incognito"), desc="brave incognito"),
        Key(
            [mod, "control"],
            "w",
            lazy.spawn("firefox --private"),
            desc="firefox incognito",
        ),
        Key([mod, "control", alt], "w", lazy.spawn("qutebrowser"), desc="qutebrowser"),
        # Applications
        Key([mod], "c", lazy.spawn("teams-for-linux"), desc="teams"),
        Key([mod, "control"], "c", lazy.spawn("outlook-for-linux"), desc="outlook"),
        Key([mod, alt], "c", lazy.spawn("telegram"), desc="telegram"),
        Key([mod], "e", lazy.spawn("emacs"), desc="emacs"),
        Key(
            [mod],
            "d",
            lazy.spawn("sh -c " + home + "/.scripts/rofi-pdf-viewer.sh"),
            desc="show menu of pdfs in ~/Documents/pdf",
        ),
        # pwd manager
        Key([mod], "p", lazy.spawn("rofi-rbw"), desc="rofi-rbw password manager"),
        Key(
            [mod, "shift"],
            "p",
            lazy.spawn("st -e rbw unlock"),
            desc="unlock password manager",
        ),
        Key(
            [mod, "control"],
            "p",
            lazy.spawn(
                'sh -c \'rbw lock && notify-send "password manager locked" || notify-send -u critical "Could not lock manager!"\''
            ),
            desc="lock password manager",
        ),
        # Bluetooth
        Key(
            [mod],
            "b",
            lazy.spawn("sh -c " + home + "/.scripts/bluetooth_connect.sh"),
            desc="unlock password manager",
        ),
        Key(
            [mod, "control"],
            "b",
            lazy.spawn("sh -c " + home + "/.scripts/bluetooth_disconnect.sh"),
            desc="unlock password manager",
        ),
        # background
        Key(
            [mod, alt],
            "b",
            lazy.spawn("sh -c " + home + "/.scripts/switch-wallpaper.sh"),
            desc="switch wallpaper",
        ),
        # Move widnows
        Key([mod, "shift"], "h", lazy.layout.swap_left(), desc="Move window to left"),
        Key([mod, "shift"], "l", lazy.layout.swap_right(), desc="Move window to right"),
        Key(
            [mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window to down"
        ),
        Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window to up"),
        Key([mod, "shift"], "f", lazy.layout.flip(), desc="Flip layout"),
        # Switch between windows
        # Some layouts like 'monadtall' only need to use j/k to move
        # through the stack, but other layouts like 'columns' will
        # require all four directions h/j/k/l to move around.
        Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
        Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
        Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
        Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
        Key(
            [mod], "space", lazy.layout.next(), desc="Move window focus to other window"
        ),
        # Grow/shrink windows left/right.
        # This is mainly for the 'monadtall' and 'monadwide' layouts
        # although it does also work in the 'bsp' and 'columns' layouts.
        Key([mod, "control"], "k", lazy.layout.grow(), desc="Grow focused window"),
        Key([mod, "control"], "j", lazy.layout.shrink(), desc="Shrink focused window"),
        # Grow windows up, down, left, right.  Only works in certain layouts.
        Key(
            [mod],
            "n",
            lazy.layout.reset().when(layout="monadtall"),
            lazy.layout.normalize().when(layout="verticaltile"),
            desc="Reset all window sizes",
        ),
        Key([mod, "shift"], "n", lazy.layout.reset(), desc="Reset slave window sizes"),
        Key(
            [mod], "m", lazy.layout.maximize(), desc="Toggle between min and max sizes"
        ),
        Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating"),
        Key(
            [mod],
            "f",
            maximize_by_switching_layout(),
            lazy.window.toggle_fullscreen(),
            desc="toggle fullscreen",
        ),
        Key(
            [mod, "shift"],
            "m",
            minimize_all(),
            desc="Toggle hide/show all windows on current group",
        ),
        # Switch focus of monitors
        Key([mod], "period", lazy.next_screen(), desc="Move focus to next monitor"),
        Key([mod], "comma", lazy.prev_screen(), desc="Move focus to prev monitor"),
    ]


"""
# Dmenu/rofi scripts launched using the key chord SUPER+p followed by 'key'
KeyChord([mod], "p", [
    Key([], "h", lazy.spawn("dm-hub -r"), desc='List all dmscripts'),
    Key([], "a", lazy.spawn("dm-sounds -r"), desc='Choose ambient sound'),
    Key([], "b", lazy.spawn("dm-setbg -r"), desc='Set background'),
    Key([], "c", lazy.spawn("dtos-colorscheme -r"), desc='Choose color scheme'),
    Key([], "e", lazy.spawn("dm-confedit -r"), desc='Choose a config file to edit'),
    Key([], "i", lazy.spawn("dm-maim -r"), desc='Take a screenshot'),
    Key([], "k", lazy.spawn("dm-kill -r"), desc='Kill processes '),
    Key([], "m", lazy.spawn("dm-man -r"), desc='View manpages'),
    Key([], "n", lazy.spawn("dm-note -r"), desc='Store and copy notes'),
    Key([], "o", lazy.spawn("dm-bookman -r"), desc='Browser bookmarks'),
    Key([], "p", lazy.spawn("rofi-pass"), desc='Logout menu'),
    Key([], "q", lazy.spawn("dm-logout -r"), desc='Logout menu'),
    Key([], "r", lazy.spawn("dm-radio -r"), desc='Listen to online radio'),
    Key([], "s", lazy.spawn("dm-websearch -r"), desc='Search various engines'),
    Key([], "t", lazy.spawn("dm-translate -r"), desc='Translate text')
])
"""
