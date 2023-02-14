#!/bin/bash

# Script: Ops 201 Class 05 Ops Challenge Solution
# Author: John Alfred Alona
# Date of latest revision: "02/13/2023"
# Purpose: Write a script using loop


echo "Kill this process using ites PID"
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
function kill_ps_aux (){
    kill -9 $(ps aux)
}

while [[ $countme2 -eq 1 ]]; do
echo "Type 1 to kill ps aux or 2 to repeat"
read pidkill

    if [[ $pidkill == "1" ]]; then
            echo "killing ps aux"
            kill_ps_aux
    elif [[ $pidkill == "2" ]]; then
            countme2=1
    else 
    echo "Stop that"
    fi
done

