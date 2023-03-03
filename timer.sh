#!/bin/bash



function timer(){
    BLUE='\033[0;34m'
    NC='\033[0m' # No Color

    echo " ${BLUE}
    ████████╗██╗███╗░░░███╗███████╗██████╗░
    ╚══██╔══╝██║████╗░████║██╔════╝██╔══██╗
    ░░░██║░░░██║██╔████╔██║█████╗░░██████╔╝
    ░░░██║░░░██║██║╚██╔╝██║██╔══╝░░██╔══██╗
    ░░░██║░░░██║██║░╚═╝░██║███████╗██║░░██║
    ░░░╚═╝░░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝"

    sleep 1
    echo "==============================================="
    sleep 1
    echo "==============================================="
    sleep 1
    echo "==============================================="
    echo ""


    echo "Do you want to shutdown your computer now or to set a timer? [1-2]"
    echo "[1] Now"
    echo "[2] Timer"
    echo ""
    read mode

    if [[ $mode == 1 ]]
    then
        sudo shutdown -h now
    elif [[ $mode == 2 ]]
    then
        echo "Please choose the time (in minutes) before the computer is powered off: "
        read timer

        echo "Timer set to " $timer " minutes. 👌👌"
        echo "To disable the timer, enter the following command: ${NC}sudo killall shutdown"
        sudo shutdown -h +$timer
    else
        echo "Wrong option entered. End of the program.💤💤"
    fi
}