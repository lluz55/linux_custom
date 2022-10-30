#! /bin/bash
CONFIGS="i3,picom,bspwm,bspwm keys,polybar,fish, ,open configs"

CONFIG_SELECTED=$( echo $CONFIGS | tr ',', '\n' |  rofi -dmenu -p "Select a config file")

case "$CONFIG_SELECTED" in
    "i3")
        alacritty -e nvim ~/.config/i3/config
        ;;
    "picom")
        alacritty -e nvim ~/.config/picom/picom.conf
        ;;
    "bspwm keys")
        alacritty -e nvim ~/.config/bspwm/sxhkdrc
        ;;
    "bspwm")
        alacritty -e nvim ~/.config/bspwm/bspwmrc
        ;;
    "fish")
        alacritty -e nvim ~/.config/fish/config.fish
        ;;
    "open configs")
        alacritty -e nvim ~/.config/rofi/scripts/open_configs.sh
        ;;
    "polybar")
        alacritty -e nvim ~/.config/polybar/material/
        ;;
    *)
        ;;
esac
