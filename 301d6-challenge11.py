#!/usr/bin/env python3

# Script: Ops 301 Class 11 Ops Challenge Solution
# Author: John Alfred C. Alona
# Date of latest revision: "03/27/2023"
# Purpose: 
import psutil
# Time spent by normal processes executing in user mode
# Time spent by processes executing in kernel mode
# Time when system was idle
# Time spent by priority processes executing in user mode
# Time spent waiting for I/O to complete.
# Time spent for servicing hardware interrupts
# Time spent for servicing software interrupts
# Time spent by other operating systems running in a virtualized environment
# Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel
lab11 = input("Please type file name for script output: ")
f = open(lab11, "w")
g = psutil.cpu_times()
h = open(lab11, "a")
h.write(str(g))
h.close()

