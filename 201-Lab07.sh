# Script: Ops 201 Class 03 Ops Challenge Solution
# Author: John Alona
# Date of latest revision: "02/15/2023"
# Purpose: Create a script that uses lshw with the following components
 
sudo lshw | grep -A 7 "*-cpu" | grep -v "capabilities" | grep -v "version" 
            # CPU
                # Product
                # Vendor
                # Physical ID
                # Bus info
                # Width

sudo lshw | grep -A 3 "*-memory"
            # RAM
                # Description
                # Physical ID
                # Size

sudo lshw | grep -A 12 "*-display" | grep -v "logical name" | grep -v "version"
            # Display adapter
                # Description
                # Product
                # Vendor
                # Physical ID
                # Bus info
                # Width
                # Clock
                # Capabilities
                # Configuration
                # Resources

sudo lshw | grep -A 15 "*-network"              
            # Network adapter
                # Description
                # Product
                # Vendor
                # Physical ID
                # Bus info
                # Logical name
                # Version
                # Serial
                # Size
                # Capacity
                # Width
                # Clock
                # Capabilities
                # Configuration
                # Resources

function dmidecode1 (){
    sudo dmidecode -t bios
}

decode=1
while [[ $decode -eq 1 ]]; do
    echo  "do you want to run dmidecode bios information?yes/no"
    read dmi


        if [[ $dmi == "yes" ]]; then    
                echo "running dmidecode bios information"
                dmidecode1
                decode=0
        elif [[ $dmi == "no" ]]; then
                echo "okay, we are done."
                decode=0
        else echo "Incorrect input, Please enter yes or no"
                decode=1
        fi
done