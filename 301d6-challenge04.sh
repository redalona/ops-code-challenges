
# Script: Ops 301 Class 04 Ops Challenge Solution
# Author: John Alfred C. Alona
# Date of latest revision: "03/16/2023"
# Purpose: 

# a bash script that launches a menu system with the following options:
# Hello world (prints “Hello world!” to the screen)
# Ping self (pings this computer’s loopback address)
# IP info (print the network adapter information for this computer)
# Exit
echo "Hello! what can I help you with?"
echo "1. Hello World"
echo "2. Ping Self"
echo "3. Network Adapter Information"
echo "4. Exit"

# Next, the user input should be requested.
# The program should next use a conditional statement to evaluate the user’s input, then act according to what the user selected.
# Use a loop to bring up the menu again after the request has been executed.
countme1=1
while [[ $countme1 == "1" ]]; do

  echo "Please select from 1-4."
  read command
    if [[ $command == "1" ]]; then
      echo "Hello World"
      countme1=1
    elif [[ $command == "2" ]]; then
      read -p "Type your ping: " ping1
      ping $("ping1")
      countme1=1
    elif [[ $command == "3" ]]; then
      lshw
      countme1=1
    elif [[ $command == "4" ]]; then
      echo "TERMINATING!!!"
      countme1=0
    else "Please only select from 1-4"
      countme1=1
    fi
done
