# Script: Ops 301 Class 13 Ops Challenge Solution
# Author: John Alona
# Date of latest revision: "03/29/2023"
# Purpose:

# Write a Powershell script that adds the below person to AD.
#     Franz Ferdinand is the TPS Reporting Lead at GlobeX USA in Springfield, OR office. Franz is part of the TPS Department. Franz’s email is ferdi@GlobeXpower.com.
New-Aduser -Name "Franz Ferdinand" -GivenName "Franz" -Surname "Ferdinand" -SamAccountName "FFerdinand" -Title "TPS Reporting Lead" -company "Globex USA" -Office "Springfield, OR" -Department "TPS" -EmailAddress "ferdi@Globexpower.com"

# Stretch Goals (Optional Objectives)
# Pursue stretch goals if you are a more advanced user or have remaining lab time.
# Have your script also create a new group in AD.
# Have your script also create a new OU in AD.