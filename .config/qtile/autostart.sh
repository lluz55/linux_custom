#!/bin/sh
setxkbmap -layout 'us,br' -option 'grp:shift_caps_toggle'
xrandr --output HDMI-0 --mode 1920x1080 --rate 60.00 --output DP-0 --mode 1920x1080 --rate 120.00 --primary --right-of HDMI-0
numlockx on
feh --bg-fill /home/lluz/Imagens/cbp2077.png &
picom &
