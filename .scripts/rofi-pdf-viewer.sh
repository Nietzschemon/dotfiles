#!/bin/sh

# build a temporary config directory
zathura_tmp=$(mktemp -d)
# build the zathura directory

# generate a config file
echo "# temporary zathura config" > "$zathura_tmp/zathurarc"

# get original options
[ -f $XDG_CONFIG_HOME/zathura/zathurarc ] && cat "$XDG_CONFIG_HOME/zathura/zathurarc" >> "$zathura_tmp/zathurarc" || \
[ -f $HOME/.config/zathura/zathurarc ] && cat "$HOME/.config/zathura/zathurarc" >> "$zathura_tmp/zathurarc" 

# add the colors
genzathurarc >> "$zathura_tmp/zathurarc"
PATH="/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin:/usr/local/sbin:/usr/local/bin:/"
#zathura --config-dir="$zathura_tmp" 

PDF_PATH=$( ls -d ~/Documents/pdf/* | rofi -dmenu -matching fuzzy)
if [[ $PDF_PATH ]]; then
 zathura $PDF_PATH --config-dir="$zathura_tmp"
fi

