#!/bin/bash
#only use this  for  transcive module
# Function to check if the script is run with root privileges
is_root() {
  if [[ $EUID -ne 0 ]]; then
    echo "This script requires root privileges. Please run with sudo."
    exit 1
  fi
}

# Call the is_root function to verify permissions
is_root

# Set appropriate permissions for /dev/ttyS0 (consider group or user access)

sudo chmod g+rw /dev/ttyS0

if [[ "$1" == "1" ]]; then
  python test_tranmiter.py
elif [[ "$1" == "0" ]]; then
  python test_reciver.py
else
  echo "Invalid argument. Please provide 1 (transmitter) or 0 (receiver)."
  exit 1
fi
