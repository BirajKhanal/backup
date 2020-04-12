#! /bin/bash

card=$(glxinfo | grep "OpenGL vendor" | cut -d ' ' -f 4)
display=$(grep 'eDP' /home/biraj/.config/polybar/config | cut -d ' ' -f 3)
display1=$(grep 'HDMI' /home/biraj/.config/polybar/config | cut -d ' ' -f 3)

if [ $card == "NVIDIA" ]
then
    source ~/.screenlayout/screen.sh & 
    feh --bg-scale /home/biraj/.config/wallpaper.jpg &
    xinput set-prop 12 336 1
else
    feh --bg-scale /home/biraj/.config/wallpaper.jpg &
    xinput set-prop 12 308 1
fi

if [ $card == "NVIDIA" ] && [ $display == "eDP-1" ] && [ $display1="HDMI-1" ]
then
    sed -i 's/eDP-1/eDP-1-1/g' /home/biraj/.config/polybar/config
    sed -i 's/HDMI-1/HDMI-1-1/g' /home/biraj/.config/polybar/config
fi

if [ $card == "Intel" ] && [ $display == "eDP-1-1" ] && [ $display1="HDMI-1-1" ]
then
    sed -i 's/eDP-1-1/eDP-1/g' /home/biraj/.config/polybar/config
    sed -i 's/HDMI-1-1/HDMI-1/g' /home/biraj/.config/polybar/config
fi


