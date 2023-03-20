#!/usr/bin/env python3

# Script: Ops 301 Class 06 Ops Challenge Solution
# Author: John Alfred C. Alona
# Date of latest revision: "03/20/2023"
# Purpose: In Ubuntu, create a Python script that executes a few bash commands successfully. Indicate in comments how you achieved this
# Requirements:

# The Python module “os” must be utilized
import os
# At least three variables must be declared in Python that contain results of bash operations
var1 = ["whoami"]
var2 = ["ip a"]
var3 = ["lshw -short"]
# The Python function print() must be used at least three times
# Include execution of the following bash commands inside your Python script:
# whoami
# ip a
# lshw -short

for item in var1:
    print(item)
    os.system("whoami")

for item in var2:
    print(item)    
    os.system("ip a")
for item in var3:
    print(item)
    os.system("lshw -short")