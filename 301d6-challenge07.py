#!/usr/bin/env python3

# Script: Ops 301 Class 07 Ops Challenge Solution
# Author: John Alfred C. Alona
# Date of latest revision: "03/21/2023"
# Purpose: Create a Python script that generates all directories, sub-directories and files for a user-provided directory path.
# Requirements:
# Script must ask the user for a file path and read a user input string into a variable.
# Script must use the os.walk() function from the os library.
# Script must enclose the os.walk() function within a python function that hands it the user input file path.

import os

# Declaration of variables
### Read user input here into a variable
fp = input("Please Input File Path: " or "default  value")
print("File path is: " + fp)
# Declaration of functions
### Declare a function here

for (root, dirs, files) in os.walk(fp):
    ## Add a print command here to print ==root==
    print(root)
    ### Add a print command here to print ==dirs==
    print(dirs)
    ### Add a print command here to print ==files==
    print(files)

# Main


### Pass the variable into the function here

# End