#!/bin/bash
is_root() {
  if [[ $EUID -ne 0 ]]; then
    echo "This script requires root privileges. Please run with sudo."
    exit 1
  fi
}
if [ $1 -eq 0 ]; then
	echo "Error no arugments provided"
	echo "enter what is transmited:\n\r 1:hello world \n\r 2:text file \n\r 3:csv file \n\r 4:PNG\n"
	exit 1
fi
# Call the is_root function to verify permissions
is_root
sudo chmod g+rw /dev/ttyS0
#get current time
current_time=$(date +%H:%M)
current_hour=$(echo $current_time | cut -d: -f 1)
previous_hour=$((current_hour-1))

while [ $current_hour -ne "12" ]&&[ $current_hour -ne "9" ]; do
  if [ $current_hour -eq $((previous_hour+1)) ]; then
    # python /home/mistaherd/Documents/Github/meshnetwork_in_forest/main/main.py
    python main/main.py
    echo "file ran successfully"
    sleep 3600
  fi
  # break #becuase everyone needs a break sometime 
done

