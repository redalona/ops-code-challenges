#!/usr/bin/python3

# Script: Ops 401 Class 03 Ops Challenge Solution
# Author: John Alfred C. Alona
# Date of latest revision: 04/19/2023
# Purpose: 

# Ask the user for an email address and password to use for sending notifications.
# Send an email to the administrator if a host status changes (from “up” to “down” or “down” to “up”).
# Clearly indicate in the message which host status changed, the status before and after, and a timestamp of the event.

import datetime, time, os
import smtplib
from datetime import datetime
from getpass import getpass

up = "Network is up"
down = "Network is down"
last = 0
ping_result = 0
email = input("Email: ")
password = getpass("Password: ")
add = input("Please provide Ping Address: ")

def up_alert():
    ct = datetime.datetime.now()
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login(email,password)
    s.sendmail("401Class02@email.com", email, "Your server is up")
    s.quit()

def down_alert():
    ct = datetime.datetime.now()
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login(email,password)
    s.sendmail("401Class02@email.com", email, "Your server is down")
    s.quit()

def ping_test(add):
    response = os.system("ping -c 1 " + add)
    if ((ping_result == 0) and (ping_result == 0)):
        last = up
        up_alert()
        ctime = datetime.now()
        print(ctime)
    elif ((ping_result != 0) and (ping_result == 0)):
        last = down
        down_alert()
        ctime = datetime.now()
        print(ctime)

while True:
    ping_test(add)
    time.sleep(2)
