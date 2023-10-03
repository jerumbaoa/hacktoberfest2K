#!/bin/bash

# Default values
DISPLAY_DISK_SPACE=false
DISPLAY_CPU_USAGE=false
DISPLAY_MEMORY_USAGE=false
DISPLAY_NETWORK_STATS=false
DISPLAY_LOGIN_DETAILS=3

# Parse command line options
while [[ $# -gt 0 ]]; do
  case $1 in
    -d|--disk)
      DISPLAY_DISK_SPACE=true
      DIRECTORY="$2"
      shift 2
      ;;
    -c|--cpu)
      DISPLAY_CPU_USAGE=true
      shift
      ;;
    -m|--memory)
      DISPLAY_MEMORY_USAGE=true
      shift
      ;;
    -n|--network)
      DISPLAY_NETWORK_STATS=true
      shift
      ;;
    -l|--login)
      DISPLAY_LOGIN_DETAILS="$2"
      shift 2
      ;;
    *)
      echo "Invalid option: $1"
      exit 1
      ;;
  esac
done

# Title
echo "*************************** SYSTEM STATUS CHECKER ***************************"

# Ask for user's name
echo "Please Enter Your Name: "
read name
echo

# Greeting
echo "********* Hi $name - Please see the detailed system status below *********"
echo " ***************************************************************************"
echo

# Display Current Date and Time
echo " **************************** Current Date and Time *************************"
date | awk ' {print "Today is: " $3 " - " $2 " ; Day = "$1 " ; Time: " $4 }'
echo

# Disk Space Available
if [ "$DISPLAY_DISK_SPACE" = true ]; then
  echo " *************************** Disk Space Available **************************"
  df -H "$DIRECTORY" | xargs | awk '{print "Disk Space Available: " "Free Used: "$10 "/" $9 " :GB" }'
  echo
fi

# CPU Usage
if [ "$DISPLAY_CPU_USAGE" = true ]; then
  echo " ***************************** CPU Usage *****************************"
  top -bn1 | grep -Po '(\d+.\d+) id' | awk '{print "CPU Usage: " 100 - $1"%"}'
  echo
fi

# Memory Usage
if [ "$DISPLAY_MEMORY_USAGE" = true ]; then
  echo " *************************** Memory Usage ***************************"
  free -h | grep -i mem | awk '{print "Total Memory: " $2 " ; Used: " $3 " ; Free: " $4}'
  echo
fi

# Network Statistics
if [ "$DISPLAY_NETWORK_STATS" = true ]; then
  echo " ************************* Network Statistics *************************"
  netstat -i
  echo
fi

# Last N Login Details
echo " ************************ Last $DISPLAY_LOGIN_DETAILS Login Details **************************"
last | head -n "$DISPLAY_LOGIN_DETAILS"
echo

# Currently Connected User
echo " **************************** Currently Connected *************************"
whoami
echo

# End
echo "******************************************* END *****************************"
