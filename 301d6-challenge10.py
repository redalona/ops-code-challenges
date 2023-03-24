#!/usr/bin/env python3

# Script: Ops 301 Class 10 Ops Challenge Solution
# Author: John Alfred C. Alona
# Date of latest revision: "03/24/2023"
# Purpose: Using file handling commands

import os
# Create a Python script that creates a new .txt file, 
lab10 = input("Input .txt file name: ")
f = open(lab10, "w")

# Appends three lines
f = open(lab10, "a")
append1 = input("Type your first append: ")
f.write(append1)
append2 = input("Type your second append: ")
f.write("\n" + append2)
append3 = input("Type your last append: ")
f.write("\n" + append3)
f.close
# Prints to the screen the first line
f = open(lab10, "r")
print(f.readlines(1))
# Then Deletes the .txt file.
os.remove(lab10)

