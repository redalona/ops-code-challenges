#!/bin/bash

# Script: Ops 201 Class 03 Ops Challenge Solution
# Author: John Alona
# Date of latest revision: "02/08/2023"
# Purpose: Write a script that prints the login history of users on this computer


#Main 
last
function LOG_IN_HISTORY {
firstname="John Alfred"
lastname="Alona"
reply="He is Learning"
noreply="Help!"

if [ "$firstname" == "John Alfred" ]; then
    echo "Struggling is learning! Keep it up!"
else
    echo "$noreply"
fi
}
# testing code
LOG_IN_HISTORY