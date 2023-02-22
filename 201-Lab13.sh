#!/bin/bash

# Script: Ops 201 Class 13 Ops Challenge Solution
# Author: John Alfred Alona
# Date of latest revision: "02/22/2023"
# Purpose: Add to your bash script a sixth option that calls a function to:

GoogleMD= touch "google.md"
function whoisgoogle {
    whois google.com
    dig google.com
    host google.com
    nslookup google.com
    
}
$GoogleMD
whoisgoogle >google.md
