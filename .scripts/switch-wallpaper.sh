#! /bin/sh
WP=$HOME/Pictures/wallpapers
WALLPAPER="$WP/$(ls $WP | shuf -n 1)"
xwallpaper --stretch $WALLPAPER
wal -i $WALLPAPER
