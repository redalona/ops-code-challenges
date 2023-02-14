#!/bin/bash

# Script: Ops 201 Class 06 Ops Challenge Solution
# Author: John Alfred Alona
# Date of latest revision: "02/13/2023"
# Purpose: Detect and create file or directory if it does or does not exist


# Create a script that detects if a file or directory exists, then creates it if it does not exist.
# Your script must use at least one array, one loop, and one conditional

function mkdir1 (){
    mkdir dir1 dir2 dir3 dir4
}

count0=1
while [[ $count0 -eq 1 ]]; do
    echo "do you want to create new directories?yes or no"
    read array
        if [[ $array == "yes" ]]; then
            mkdir1
            count0=1
        elif [[ $array == "no" ]]; then
            count0=0
        else echo "Hello? Wrong input!"
            count0=1
        fi
done

#creating text file

function toucharray () {
array1=("./dir1/" "./dir2/" "./dir3/" "./dir4/")   
    touch "${array1[0]}file.txt"
    touch "${array1[1]}file.txt"
    touch "${array1[2]}file.txt"
    touch "${array1[3]}file.txt"
}

count1=1

while [[ $count1 -eq 1 ]]; do
    
    echo "do you want to create new files?yes or no"
    read touch
    
        if [[ $touch == "yes" ]]; then
        toucharray
        count1=0
        echo Done!
        elif [[ $touch == "no" ]]; then
        echo "terminating......."
        echo "Done!"
        count1=0
        else echo "You are better than that!"
        count1=1
        fi
done



