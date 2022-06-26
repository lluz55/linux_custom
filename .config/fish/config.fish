if status is-interactive
  # Commands to run in interactive sessions can go here
  alias c='clear'
  alias lh='ls -hlF'
  alias timev='/usr/bin/time -v'
  alias up='sudo apt update ; sudo apt upgrade -y'
  alias inst='sudo apt install'
  alias search='apt search'
  alias upg='sudo apt dist-upgrade -y'
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
  alias vmup='sudo apt install linux-headers-`(uname -r)`'
  alias mfiles='sudo mount -t ntfs-3g -o rw /dev/sdb1 /media/lluz/Files'
  alias cgmset='sudo cgmemtime --setup -g lluz --perm 775'
  alias fdev='cd ~/dev'
  alias snapi='sudo snap install '
  alias v='nvim'
  alias sdn='shutdown now'
  alias sdr='shutdown -r now'
  alias upd='sudo apt update ; sudo apt upgrade -y ; sudo apt dist-upgrade'

  alias ls='/opt/coreutils/bin/ls'
  alias gitc='mkdir $HOME/tmp ; cd $HOME/tmp/ ; git clone '
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

