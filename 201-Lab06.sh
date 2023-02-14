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
    echo "do you want to create a new directory?"
    read array
        if [[ $array == "yes" ]]; then
            mkdir1
            count0=1
        elif [[ $array == "no" ]]; then
            echo "do you want to create a new file?"
            count0=2
        else echo "Hello?"
        fi
done

#creating text file
function touch1 (){
    touch "${array1[0]}file.txt"
    touch "${array1[1]}file.txt"
    touch "${array1[2]}file.txt"
    touch "${array1[3]}file.txt"
}
count1=1
while [[ $count1 -eq 1 ]]; do
    read touch
        if [[ $touch == "yes" ]]; then
        touch1
        elif [[ $touch == "no" ]]; then
        echo "terminating"
        count0=2
        else echo "come on!"
        fi
done