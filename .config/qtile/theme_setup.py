import os
import subprocess
from random import choice

import pywal

home = os.path.expanduser("~")
wallpaper_path = home + "/Pictures/wallpapers/"
wallpaper_random = wallpaper_path + choice(os.listdir(wallpaper_path))
special_colors = None
colors = None


def setup():
    if wallpaper_random is not None:
        subprocess.run(["xwallpaper", "--stretch", wallpaper_random])
        subprocess.run(["wal", "-i", wallpaper_random, "-n"])
        set_colors()
        return special_colors, colors

    return special_colors, colors


def get_colors():
    colors = pywal.colors.get(wallpaper_random)
    special_colors = [colors["special"]["background"], colors["special"]["foreground"]]
    colors = [
        colors["colors"]["color0"],
        colors["colors"]["color1"],
        colors["colors"]["color2"],
        colors["colors"]["color3"],
        colors["colors"]["color4"],
        colors["colors"]["color5"],
        colors["colors"]["color6"],
        colors["colors"]["color7"],
        colors["colors"]["color8"],
        colors["colors"]["color9"],
        colors["colors"]["color10"],
        colors["colors"]["color11"],
        colors["colors"]["color12"],
        colors["colors"]["color13"],
        colors["colors"]["color14"],
        colors["colors"]["color15"],
    ]
    return special_colors, colors


def set_colors():
    global special_colors, colors
    special_colors, colors = get_colors()
