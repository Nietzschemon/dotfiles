#! /bin/sh
bluetoothctl disconnect $(bluetoothctl devices Connected | dmenu | cut -d" " -f2) && notify-send "Disconnected from device" || notify-send -u critical "Could not disconnect device"
