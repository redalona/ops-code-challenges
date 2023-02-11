#!/bin/bash

# Script: Ops 201 Class 05 Ops Challenge Solution
# Author: John Alfred Alona
# Date of latest revision: "02/10/2023"
# Purpose: Write a script using loop

pid1="yes"
pid2="no"


while [[ $pid1 == "yes" ]]
    do 
        echo "do you want to execute ps aux?"
        read $pid1
    done 

    