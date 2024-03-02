#!/usr/bin/env bash 

COLORSCHEME=DoomOne


### AUTOSTART PROGRAMS ###
lxsession &
xscreensaver --no-splash &
picom --daemon &
"$HOME"/.screenlayout/defaultlayout.sh &
sleep 1
conky -c "$HOME"/.config/conky/qtile/01/"$COLORSCHEME".conf || echo "Couldn't start conky." &
