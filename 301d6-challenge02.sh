#!/bin/bash

# Script: Ops 301 Class 02 Ops Challenge Solution
# Author: John Alfred C. Alona
# Date of latest revision: "03/14/2023"
# Purpose: Copies /var/log/syslog to the current working directory
         # Appends the current date and time to the filename

cat /var/log/syslog >SysLog$(date +'%Y-%m-%dT%H:%M:%S%z')
echo you just created system log file!