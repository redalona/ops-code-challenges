# Print to the terminal screen all active processes ordered by highest CPU time consumption at the top.
Get-Process | Sort-Object cpu -Descending
# Print to the terminal screen all active processes ordered by highest Process Identification Number at the top.
Get-Process | Sort-Object id -Descending
# Print to the terminal screen the top five active processes ordered by highest Working Set (WS(K)) at the top.
get-process | Select-Object -First 5 | Sort-Object WS -Descending
# Start the process Internet Explorer (iexplore.exe) and have it open https://owasp.org/www-project-top-ten/.
Start-Process iexplore https://owasp.org/www-project-top-ten/
# Start the process Internet Explorer (iexplore.exe) ten times using a for loop. Have each instance open https://owasp.org/www-project-top-ten/.
for ($i=0; $i -le 10; $i++)
{
    Start-Process iexplore
}
# Close all Internet Explorer windows.
Stop-Process iexplore
# Kill a process by its Process Identification Number. Choose a process whose termination won’t destabilize the system, such as Internet Explorer or MS Edge.
taskkill /f /pid 6380
