#!/bin/bash

# Script: Ops 301 Class 02 Ops Challenge Solution
# Author: John Alfred C. Alona
# Date of latest revision: "03/15/2023"
# Purpose: 

#Prompts user for input directory path.
read -p "Please Enter Directory Path:" r1
dir1=$(dirname "$r1")
cd "$dir1"
#Prompts user for input permissions number (e.g. 777 to perform a chmod 777)
countme=1
while [[ $countme -eq 1 ]]; do
    echo "Allow to change permissions for directory? yes or no"
    read value

        if [[ $value == "yes" ]]; then 
            echo "Permission granted"
            countme=0
        elif [[ $value == "no" ]]; then
            echo "goodbye!"
            exit
            
        else echo "Please answer Yes or No"
            countme=1
        fi
done
#Navigates to the directory input by the user and changes all files inside it to the input setting.
read -p "Input Number:" r2
chmod1=$(chmod "$r2" "$dir1")
$chmod1
#Prints to the screen the directory contents and the new permissions settings of everything in the directory.
read -p "Read directory contents and permission settings of input directory path:" r3
dir2=$(dirname "$r3")
cd "$dir2"
awk 1 * */*
echo "Permission Setting"
ls -ld $dir2
