if status is-interactive
  # Commands to run in interactive sessions can go here

  alias c='clear'
  alias lh='ls -hlF'
  alias timev='/usr/bin/time -v'

  # Install nala [frontend for apt package manager]
  # https://ostechnix.com/nala-commandline-frontend-for-apt/
  alias up='sudo nala update ; sudo nala upgrade -y'
  alias vmup='sudo nala install linux-headers-`(uname -r)`'
  alias inst='sudo nala install'
  alias search='nala search'
  alias upg='sudo nala dist-upgrade -y'
  alias upd='sudo nala update ; sudo nala upgrade -y ; sudo nala dist-upgrade'

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
  alias mfiles='sudo mount -t ntfs-3g -o rw /dev/sdb1 /media/lluz/Files'
  alias cgmset='sudo cgmemtime --setup -g lluz --perm 775'
  alias fdev='cd ~/dev'
  alias snapi='sudo snap install '
  alias v='nvim'
  alias lv='$HOME/.local/bin/lvim'
  alias sdn='shutdown now'
  alias sdr='shutdown -r now'

  alias ls='/opt/coreutils/bin/ls'
  alias gitc='mkdir $HOME/tmp ; cd $HOME/tmp/ ; git clone '
  alias nk='kitty -e fish &' #open new kitty window and launch fish in current directory
  set fish_greeting ""
  
# Changing "ls" to "exa"
   alias ls='exa --icons --color=always --group-directories-first'
   alias ll='exa -alF --icons --color=always --group-directories-first'
   alias la='exa -a --icons --color=always --group-directories-first'
   alias l='exa -F --icons --color=always --group-directories-first'
   alias l.='exa -a | egrep "^\."'

   #fastfetch
#neofetch
end

zoxide init fish | source

# Generated for envman. Do not edit.
test -s "$HOME/.config/envman/load.fish"; and source "$HOME/.config/envman/load.fish"

# use LunarVim as sudo editor
# sudoedit
set -x EDITOR $HOME/.local/bin/lvim 

# set variable for PKG_CONFIG_PATH
set PKG_CONFIG_PATH /usr/lib/x86_64-linux-gnu/pkgconfig

# pkg_config
set PKG_CONFIG /usr/bin/pkgconfig

exec nu
