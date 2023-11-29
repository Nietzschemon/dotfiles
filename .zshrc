# Luke's config for the Zoomer Shell

# Jumps into tmux at start up IF tmux is not running
# tmux ls 2> /tmp/NULL > /tmp/NULL || tmux

# Enable colors and change prompt:
autoload -U colors && colors
PS1="%B%{$fg[blue]%}[%{$fg[yellow]%}%n%{$fg[blue]%}@%{$fg[red]%}%M %{$fg[magenta]%}%~%{$fg[blue]%}]%{$reset_color%}$%b "

# History in cache directory:
HISTSIZE=100000
SAVEHIST=100000
HISTFILE=~/.cache/zsh/.zsh_history
setopt INC_APPEND_HISTORY_TIME #<- adds commadns to history file at once
#export HISTTIMEFORMAT="[%F %T] "
setopt EXTENDED_HISTORY

function zshaddhistory() {
  emulate -L zsh
  whence ${${(z)1}[1]} >| /dev/null || return 1
}

# Basic auto/tab complete:
autoload -U compinit
zstyle ':completion:*' menu select
zmodload zsh/complist
compinit
_comp_options+=(globdots)		# Include hidden files.

# vi mode
bindkey -v
export KEYTIMEOUT=1

# Use vim keys in tab complete menu:
bindkey -M menuselect 'h' vi-backward-char
bindkey -M menuselect 'k' vi-up-line-or-history
bindkey -M menuselect 'l' vi-forward-char
bindkey -M menuselect 'j' vi-down-line-or-history
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

# Use lf to switch directories and bind it to ctrl-o
lfcd () {
    tmp="$(mktemp)"
    lf -last-dir-path="$tmp" "$@"
    if [ -f "$tmp" ]; then
        dir="$(cat "$tmp")"
        rm -f "$tmp"
        [ -d "$dir" ] && [ "$dir" != "$(pwd)" ] && cd "$dir"
    fi
}
bindkey -s '^o' 'lfcd\n'

# Edit line in vim with ctrl-e:
autoload edit-command-line; zle -N edit-command-line
bindkey '^e' edit-command-line

# Load aliases and shortcuts if existent.
[ -f "$HOME/.config/shortcutrc" ] && source "$HOME/.config/shortcutrc"
[ -f "$HOME/.config/aliasrc" ] && source "$HOME/.config/aliasrc"

export LESS_TERMCAP_mb="$(printf '%b' '[1;31m')"
export LESS_TERMCAP_md="$(printf '%b' '[1;36m')"
export LESS_TERMCAP_me="$(printf '%b' '[0m')"
export LESS_TERMCAP_so="$(printf '%b' '[01;44;33m')"
export LESS_TERMCAP_se="$(printf '%b' '[0m')"
export LESS_TERMCAP_us="$(printf '%b' '[1;32m')"
export LESS_TERMCAP_ue="$(printf '%b' '[0m')"
export PATH="$HOME/.npm-global/bin:$PATH"

setxkbmap -layout se -variant nodeadkeys -option caps:escape

# Sets git config for managing dotfiles 
alias config='/usr/bin/git --git-dir=/home/stefan//.cfg/ --work-tree=/home/stefan/'

#alias vim='nvim'

# Loads sqlite-history
source $HOME/.gitrepos/zsh-histdb/sqlite-history.zsh
autoload -Uz add-zsh-hook
# Sets reverse search
source $HOME/.gitrepos/zsh-histdb/histdb-interactive.zsh
bindkey '^r' _histdb-isearch

source /usr/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

if systemctl -q is-active graphical.target && [[ ! $DISPLAY && $XDG_VTNR -eq 1 ]]; then
  exec startx
fi

