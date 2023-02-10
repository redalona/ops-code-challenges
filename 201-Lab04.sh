#!/bin/bash

# Script: Ops 201 Class 04 Ops Challenge Solution
# Author: John Alona
# Date of latest revision: "02/09/2023"
# Purpose: Write a script using array

# Create four directories
mkdir dir1 dir2 dir3 dir4

# Put the names of the four directories in an array

array1=("./dir1/" "./dir2/" "./dir3/" "./dir4/")

touch "${array1[0]}file.txt"
touch "${array1[1]}file.txt"
touch "${array1[2]}file.txt"
touch "${array1[3]}file.txt"


