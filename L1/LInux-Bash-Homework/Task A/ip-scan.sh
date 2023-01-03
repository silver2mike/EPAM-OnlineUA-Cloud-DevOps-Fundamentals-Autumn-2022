#!/bin/bash
#
# Scaning the specific network to find live hosts and open ports
# Keys:
# --all [Network (10.10.10.0/24]	- display all available hosts inside the network
# --target [IP address] 		- display open ports 
#
#

#NETW="192.168.0.103/24"
NETW=$2

function all {
   echo "All available hosts in $NETW:"
   nmap -R -sP $NETW | grep "Nmap scan report for" | sed 's/Nmap scan report for //g'
}

function target () {
   echo "Open system TCP ports for $1"
   nmap -sT $1 | tail -n +6 | head -n -3
}

### MAIN ###

if [ "$1" == "--all" ]; then
   all
elif [ "$1" == "--target" ] && [ "$2" != "" ]; then
   target $2
else
   echo " Use the following arguments"
   echo " --all [Network e.g. 10.10.10.0/24] to display the IP addresses and symbolic names of all hosts in the current subnet"
   echo " --target [TARGET IP] to display a list of oper system TCP ports"
fi
