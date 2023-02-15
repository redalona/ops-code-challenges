# Script: Ops 201 Class 03 Ops Challenge Solution
# Author: John Alona
# Date of latest revision: "02/08/2023"
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