#!/bin/sh

card=$(glxinfo | grep "OpenGL vendor"| cut -d ' ' -f 4)

if [ $card='NVIDIA' ]
then
    source ~/.screenlayout/screen.sh & 
    feh --bg-scale /home/biraj/.config/wallpaper.jpg &
    qtile-cmd -o cmd -f restart &
else
    feh --bg-scale /home/biraj/.config/wallpaper.jpg &
fi

xset led on
xinput set-prop 12 308 1
flameshot &
nm-applet &
picom --config ~/.config/compton/compton.conf  &
optimus-manager-qt &
