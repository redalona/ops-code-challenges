#!/bin/bash

# Script: Ops 201 Class 05 Ops Challenge Solution
# Author: John Alfred Alona
# Date of latest revision: "02/13/2023"
# Purpose: Write a script using loop

function kill1 (){
    exec $(kill  201-Lab05.sh)
}

echo "Kill this process using it's PID"
#PID
countme=1
while [[ $countme -eq 1 ]]; do
    echo "do you want to run ps aux to get PID? (yes or no)"
    read pid

        if [[ $pid == "yes" ]]; then
             ps aux
            countme=1
        elif [[ $pid == "no" ]]; then
             echo "proceed to kill tihs process"
            break
        else echo "that was nonsense"
             countme=1
        fi
done

#kill PID
countme2=1

while [[ $countme2 -eq 1 ]]; do
    echo "Please kill this process using PID. (type 1 to kill this process, 2 to repeat this instruction)"
    read lab05
    if [[ $lab05 == "1" ]]; then
        kill1
    elif [[ $lab05 == "2" ]]; then
        echo "repeating instruction"
        countme2=1
    else echo "stop making nonsense"
    fi
done

