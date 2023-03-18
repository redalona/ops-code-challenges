#!/bin/bash

# Script: Ops 301 Class 05 Ops Challenge Solution
# Author: John Alfred C. Alona
# Date of latest revision: "03/17/2023"
# Purpose: 
# Write a bash script that performs the following tasks:
# Print to the screen the file size of the log files before compression
echo "File size are shown in bytes"
echo "syslog"
wc -c /var/log/syslog | awk '{print $1}' 
echo "wtmp"
wc -c /var/log/wtmp | awk '{print $1}'
# Compress the contents of the log files listed below to a backup directory
echo "Compress the contents of /var/log/syslog and /var/log/wtmp to a backup directory"
count1=1
read -p "Please type backup directory:" backup
    if [[ -d "$backup" ]]; then
        echo "Directory found, Proceed to compressing log contents" 
    else echo "Directory not found, Creating new directory"
        mkdir $backup 
    fi
# /var/log/syslog
echo "Compressing syslog to backup directory"
sudo zip -r /var/log/syslog$(date '+%Y%m%d%H%M%S') /var/log/syslog
# /var/log/wtmp
# The file name should contain a time stamp with the following format -YYYYMMDDHHMMSS
# Example: /var/log/backups/syslog-20220928081457.zip
# Clear the contents of the log file
# Print to screen the file size of the compressed file
# Compare the size of the compressed files to the size of the original log file