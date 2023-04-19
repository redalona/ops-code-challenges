#!/usr/bin/python3

# Script: Ops 401 Class 02 Ops Challenge Solution
# Author: John Alfred C. Alona
# Date of latest revision: 04/18/2023
# Purpose: 

import os, time
from datetime import datetime
# Transmit a single ICMP (ping) packet to a specific IP every two seconds.
# Evaluate the response as either success or failure.
#Assign success or failure to a status variable.
#For every ICMP transmission attempted, print the status variable along with a comprehensive timestamp and destination IP tested.
#Example output: 2020-10-05 17:57:57.510261 Network Active to 8.8.8.8


pingwhat = input("Enter Ping Address: ")
while True:
    ping = os.system("ping -c 1 " + pingwhat)
    if ping == 0:
        time.sleep(2)
        print(ping)
        print("Ping Successful")
        ctime = datetime.now()
        print(ctime)
    else:
        time.sleep(2)
        print(ping)
        print("Ping Unsuccessful")
        ctime = datetime.now()
        print(ctime)
