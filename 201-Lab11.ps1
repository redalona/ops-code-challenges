# Script: Ops 201 Class 04 Ops Challenge Solution
# Author: John Alona
# Date of latest revision: "02/09/2023"
# Purpose: Write a script using array

# Enable File and Printer Sharing
Set-NetFirewallRule -DisplayGroup "File And Printer Sharing" -Enabled True

# Allow ICMP traffic
netsh advfirewall firewall add rule name="Allow incoming ping requests IPv4" dir=in action=allow protocol=icmpv4 

# Enable Remote management
# RDP
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f
# NLA
Set-ItemProperty ‘HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp\‘ -Name “UserAuthentication” -Value 1
#Firewall Rule
Enable-NetFirewallRule -DisplayGroup “Remote Desktop”

# Remove bloatware
iex ((New-Object System.Net.WebClient).DownloadString('https://git.io/debloat'))

# Enable Hyper-V
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All

# Disable SMBv1, an insecure protocol
Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force

# Did your script enable File and Printer Sharing? 
# What did you do to test before/after?
# Did your script allow ICMP traffic?
# What did you do to test before/after?
# Did your script enable Remote management?
# What did you do to test before/after?
# Did your script remove bloatware?
# What did you do to test before/after?
# Did your script enable Hyper-V?
# What did you do to test before/after?
# Did your script disable SMBv1?
# What did you do to test before/after?