#! /bin/sh
bluetoothctl connect $(bluetoothctl devices Paired | dmenu | cut -d" " -f2) && notify-send "Connected to device" || notify-send -u critical "Could not connect to device"

