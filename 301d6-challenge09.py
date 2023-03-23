#!/usr/bin/env python3

# Script: Ops 301 Class 09 Ops Challenge Solution
# Author: John Alfred C. Alona
# Date of latest revision: "03/23/2023"
# Purpose:
# Create if statements using these logical conditionals below. Each statement should print information to the screen depending on if the condition is met.
a = 100
b = 200

Equals: a == b
if a == b:
    print("is", a, "==", b)
    print(a, "is equal to", b)
# Not Equals: a != b
if a != b:
    print("is", a, "!=", b)
    print(a, "is not equal", b)
# Less than: a < b
if a < b:
    print("is", a, "<", b)
    print(a, "is less than", b)
# Less than or equal to: a <= b
if a <= b:
    print("is", a, "<=", b)
    if a < b:
        print(a, "is less than", b)
    if a == b:
        print(a, "is equal to", b)
# Greater than: a > b
if a > b:
    print("is", a, ">", b)
    print(a, "is greater than", b)
# Greater than or equal to: a >= b
if a >= b:
    print("is", a, "">="", b)
    if a > b:
        print(a, "is greater than", b)
    if a == b:
        print(a, "is equal to", b)
#Create an if statement using a logical conditional of your choice and include elif keyword that executes when other conditions are not met.

logelseif = input("Type any number here: ")

try:
    logelseif = int(logelseif)
    if int(logelseif) > a:
        print(logelseif, "is greater than", a)
        if int(logelseif) < b:
            print(logelseif, "is greater than", a, "but is less than", b)
        if int(logelseif) == b:
            print(logelseif, "is equal to", b)
        else:
            print(logelseif, "is greater than", b)
# Create an if statement that includes both elif and else to execute when both if and elif are not met.   
    elif int(logelseif) < a:
        print(logelseif, "is less than", a)
    else:
        print(logelseif, "is equal", a)
except ValueError:
    print(logelseif, "is invalid It is not a number.")


