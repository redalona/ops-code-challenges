# Script: Ops 201 Class 12 Ops Challenge Solution
# Author: John Alona
# Date of latest revision: "02/21/2023"
# Purpose: Create a Powershell script that performs the following operations:

# Create a local file called network_report.txt that holds the contents of an ipconfig /all command.
ipconfig /all >network_report.txt

# Use Select-String to search network_report.txt and return only the IP version 4 address.
function net_rep {
    Select-String -Path .\network_report.txt -Pattern "IPv4"
}
net_rep
# Remove the network_report.txt when you are finished searching it.
Remove-Item -Path .\network_report.txt