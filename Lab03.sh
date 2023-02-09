#!/bin/bash

# Script: Ops 201 Class 03 Ops Challenge Solution
# Author: John Alona
# Date of latest revision: "02/08/2023"
# Purpose: Write a script that prints the login history of users on this computer

last
function LOG_IN_HISTORY {
LogInHistory="$(hostname)"
initiate="$last"

if [ "$loginhistory" == "$hostname" ]; then
    echo "$initiate"
fi
}
LOG_IN_HISTORY