#!/bin/bash

copied=0

function sync_in {
    echo "Syncing to backup"
    rsync -ra /home/biraj/.config/qtile /home/biraj/backup/ &
    rsync -ra /home/biraj/.config/nvim /home/biraj/backup/ &
    rsync -ra /home/biraj/.config/alacritty /home/biraj/backup/ &
    rsync -ra /home/biraj/.config/ranger /home/biraj/backup/ &
    rsync -ra /home/biraj/.zshrc /home/biraj/backup/ &
    rsync -ra /home/biraj/.config/compton /home/biraj/backup/ &
    rsync -ra /home/biraj/.config/dunst /home/biraj/backup/ &
    rsync -ra /home/biraj/scripts /home/biraj/backup/ &
    rsync -ra /home/biraj/.config/bspwm /home/biraj/backup/ &
    rsync -ra /home/biraj/.config/polybar /home/biraj/backup/ &
    rsync -ra /home/biraj/.config/sxhkd /home/biraj/backup/ &
    rsync -ra /home/biraj/.local/share/fonts /home/biraj/backup/ &
    rsync -ra /home/biraj/.local/share/icons /home/biraj/backup/ &
}

function sync_out {
    #function_body
    echo "Syncing to device"
    rsync -ra  /home/biraj/backup/qtile  /home/biraj/.config/qtile &
    rsync -ra  /home/biraj/backup/nvim  /home/biraj/.config/nvim &
    rsync -ra  /home/biraj/backup/alacritty  /home/biraj/.config/alacritty &
    rsync -ra  /home/biraj/backup/ranger  /home/biraj/.config/ranger &
    rsync -ra  /home/biraj/backup/.zshrc  /home/biraj/.zshrc &
    rsync -ra  /home/biraj/backup/compton  /home/biraj/.config/picom.conf &
    rsync -ra  /home/biraj/backup/dunst  /home/biraj/.config/dunst &
    rsync -ra  /home/biraj/backup/scripts  /home/biraj/scripts &
    rsync -ra  /home/biraj/backup/bspwm  /home/biraj/.config/bspwm &
    rsync -ra  /home/biraj/backup/polybar  /home/biraj/.config/polybar &
    rsync -ra  /home/biraj/backup/sxhkd  /home/biraj/.config/sxhkd &
    rsync -ra  /home/biraj/backup/fonts  /home/biraj/.local/share/fonts &
    rsync -ra  /home/biraj/backup/icons  /home/biraj/.local/share/icons &
}

function push {
    cd /home/biraj/backup
    git init
    git add .
    git commit -m "update"
    git push -u origin master
}

case "$1" in
    -i )
        sync_in
        ;;
    -o )
        sync_out
        ;;
    -p )
        push
        ;;
    -h )
        echo " '-o' To sync backup to pc "
        echo " '-i' To sync setting to backup "
        echo " '-p' To push the directory to git"
        ;;
     *)
        echo "-h flag for help"
        ;;
esac 
