#!/bin/bash


function addDateToFilename(){
    # Load in the functions and animations
    username=$(whoami)
    locationFile=$(find /Users/${username}/Desktop/bashTools -iname "spinner.sh")
    source $locationFile


    RED='\033[0;31m'
    NC='\033[0m' # No Color



    echo " ${RED}

    ░█▀▀█ ░█▀▀▀ ░█▄─░█ ─█▀▀█ ░█▀▄▀█ ░█▀▀▀   ▀█▀ ▀▀█▀▀ 
    ░█▄▄▀ ░█▀▀▀ ░█░█░█ ░█▄▄█ ░█░█░█ ░█▀▀▀   ░█─ ─░█── 
    ░█─░█ ░█▄▄▄ ░█──▀█ ░█─░█ ░█──░█ ░█▄▄▄   ▄█▄ ─░█──

    "

    sleep 1
    echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    sleep 1
    echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    sleep 1
    echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    echo ""


    read -p "Please write down the extension of the files you want to rename: " extension


    echo ""
    sleep 2


    echo "Searching for files with the extension:" $extension
    spinner
    echo ""


    #Files with the intputed extension
    PICTURES=$(ls *$extension)



    if [[ $PICTURES == "" ]]
    then
        echo ""
        echo "No files with the '${extension}' extension found.\nEnd of the program💤💤"
    else
        echo "Found files having the" $extension "extension: "
        ls $PICTURES
        echo ""
        sleep 4


        #Today's date
        DATE=$(date +%F)

        for PICTURE in $PICTURES
        do
            echo "Renaming ${PICTURE} to ${DATE}-${PICTURE}"
            mv ${PICTURE} ${DATE}-${PICTURE}
        done
    fi
}