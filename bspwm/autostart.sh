#! /bin/sh

bspc rule -r "*"

# to kill the application for every reload so only one instance is loaded
killall polybar bar1
killall polybar bar2
killall sxhkd
killall dunst
killall picom

#----Autostart commands----#

# application to started after login
sxhkd &
polybar bar1 &
polybar bar2 &
xset led on
flameshot &
nm-applet &
picom --config ~/.config/compton/compton.conf  &
optimus-manager-qt &
dunst &
udiskie &

