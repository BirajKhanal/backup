#! /bin/sh

bspc rule -r "*"

# to kill the application for every reload so only one instance is loaded
killall polybar bar1
killall polybar bar2
killall sxhkd
killall dunst
killall picom
killall flameshot

#----Autostart commands----#

# application to started after login
sxhkd &
polybar bar1 &
polybar bar2 &
nm-applet &
xset led on
xinput set-prop 12 341 1
xinput set-prop 12 342 1
picom --config ~/.config/picom/picom.conf &
optimus-manager-qt &
flameshot &
dunst &
udiskie &
