if status is-interactive
    # Commands to run in interactive sessions can go here
    set fish_greeting ""

    # Install nala [frontend for apt package manager]
    # https://ostechnix.com/nala-commandline-frontend-for-apt/
    ## Debian based package manager
    alias aptu='sudo nala update ; sudo nala upgrade -y'
    alias apti='sudo nala install'
    alias apts='nala search'
    alias aptd='sudo nala dist-upgrade -y'

    ## Arch based package manager
    alias pai='sudo pacman -S '
    alias yai='yay  --answerdiff None --answerclean None --removemake -S '
    alias yar='yay -R '

    ## Git aliases
    alias ga='git add '
    alias ga.='git add .'
    alias gaa='git add .'
    alias gp='git push'
    alias gpl='git pull'
    alias gcm='git commit -m'
    alias gcmu='gcm "updated"'
    alias gd='git diff'
    alias glog='git log --oneline'
    alias gc='git checkout '
    alias gst='git status'
    alias gamend='git commit --amend'
    alias gamendn='git commit --amend --no-edit'

    ## Snap
    alias snapi='sudo snap install '

    ## Neovim and flavoures
    alias v='nvim'
    alias lv='$HOME/.local/bin/lvim'

    ## Power related
    alias sdn='shutdown now'
    alias sdr='shutdown -r now'

    alias c='clear'

    ## Cargo
    alias crgi='cargo install '
    alias crgr='cargo run'
    alias crgrr='cargo run --release'
    alias crgre='cargo run --release --example '

    #Open new kitty window and launch fish in current directory
    alias nk='kitty -e fish &'


    # Changing "ls" to "exa"
    alias ls='exa --icons --color=always --group-directories-first'
    alias lll='exa -lF --icons --color=always --group-directories-first'
    alias ll='exa -alF --icons --color=always --group-directories-first'
    alias la='exa -a --icons --color=always --group-directories-first'
    alias l='exa -F --icons --color=always --group-directories-first'
    alias l.='exa -a | egrep "^\."'

    # run kitty-xterm in remote session
    alias kssh='kitty +kitten ssh '

    alias hx='helix'
    alias cfish='nvim $HOME/.config/fish/config.fish'
    alias ci3='nvim $HOME/.config/i3/config'
    alias clazy='nvim $HOME/.config/nvim/lua/plugins/example.lua'
    alias chyp='nvim $HOME/.config/hypr/hyprland.conf'

    #fastfetch
    #neofetch
end

# zoxide init fish | source

starship init fish | source

# Generated for envman. Do not edit.
test -s "$HOME/.config/envman/load.fish"; and source "$HOME/.config/envman/load.fish"

# use LunarVim as sudo editor
# sudoedit
# set -x EDITOR $HOME/.local/bin/lvim 
set -x EDITOR nvim
set -x VISUAL nvim

# Used in wayland only
set QT_QPA_PLATFORM wayland

## PKG_CONFIG
# set variable for PKG_CONFIG_PATH
set PKG_CONFIG_PATH /usr/lib/x86_64-linux-gnu/pkgconfig
# pkg_config
set PKG_CONFIG /usr/bin/pkgconfig

# ask for password start of fish session
# eval (ssh-agent -c) && ssh-add ~/.ssh/id_rsa

## Use kitty inside ssh
#alias ssh='kitty +kitten ssh'

set XDG_RUNTIME_DIR $HOME/.cache/xdgr/
