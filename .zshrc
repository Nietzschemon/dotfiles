###################################################################
######################### MANJARO CONF ############################
###################################################################
# Use powerline
USE_POWERLINE="true"
# Has weird character width
# Example:
#    is not a diamond
HAS_WIDECHARS="false"

# Source manjaro-zsh-configuration
[[ -e /usr/share/zsh/manjaro-zsh-config ]] && source ~/.config/zsh/manjaro-zsh-config
[[ -e /usr/share/zsh/manjaro-zsh-prompt ]] && source ~/.config/zsh/manjaro-zsh-prompt

###################################################################
############################## END ################################
###################################################################

# History in cache directory:
HISTSIZE=100000
SAVEHIST=100000
#HISTFILE=~/.cache/zsh/.zsh_history
#setopt INC_APPEND_HISTORY_TIME #<- adds commadns to history file at once
#export HISTTIMEFORMAT="[%F %T] "
#setopt EXTENDED_HISTORY


# vi mode
bindkey -v
export KEYTIMEOUT=1

# Use vim keys in tab complete menu:
#bindkey -M menuselect 'h' vi-backward-char
#bindkey -M menuselect 'k' vi-up-line-or-history
#bindkey -M menuselect 'l' vi-forward-char
#bindkey -M menuselect 'j' vi-down-line-or-history
bindkey -v '^?' backward-delete-char

# Change cursor shape for different vi modes.
function zle-keymap-select {
  if [[ ${KEYMAP} == vicmd ]] ||
     [[ $1 = 'block' ]]; then
    echo -ne '\e[1 q'
  elif [[ ${KEYMAP} == main ]] ||
       [[ ${KEYMAP} == viins ]] ||
       [[ ${KEYMAP} = '' ]] ||
       [[ $1 = 'beam' ]]; then
    echo -ne '\e[5 q'
  fi
}
zle -N zle-keymap-select
zle-line-init() {
    zle -K viins # initiate `vi insert` as keymap (can be removed if `bindkey -V` has been set elsewhere)
    echo -ne "\e[5 q"
}
zle -N zle-line-init
echo -ne '\e[5 q' # Use beam shape cursor on startup.
preexec() { echo -ne '\e[5 q' ;} # Use beam shape cursor for each new prompt.

# Edit line in vim with ctrl-e:
autoload edit-command-line; zle -N edit-command-line
bindkey '^e' edit-command-line

# Load aliases and shortcuts if existent.
#[ -f "$HOME/.config/shortcutrc" ] && source "$HOME/.config/shortcutrc"
[ -f "$HOME/.config/aliasrc" ] && source "$HOME/.config/aliasrc"

#export LESS_TERMCAP_mb="$(printf '%b' '[1;31m')"
#export LESS_TERMCAP_md="$(printf '%b' '[1;36m')"
#export LESS_TERMCAP_me="$(printf '%b' '[0m')"
#export LESS_TERMCAP_so="$(printf '%b' '[01;44;33m')"
#export LESS_TERMCAP_se="$(printf '%b' '[0m')"
#export LESS_TERMCAP_us="$(printf '%b' '[1;32m')"
#export LESS_TERMCAP_ue="$(printf '%b' '[0m')"
#export PATH="$HOME/.npm-global/bin:$PATH"

bindkey "^R" history-incremental-search-backward

setxkbmap -layout se -variant nodeadkeys -option caps:escape

#neofetch

# Start with random meme
jp2a --color-depth=24 ~/Pictures/mems/$(ls ~/Pictures/mems/ | shuf -n 1 )
