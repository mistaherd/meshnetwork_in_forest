#!/bin/bash
is_root() {
  if [[ $EUID -ne 0 ]]; then
    echo "This script requires root privileges. Please run with sudo."
    exit 1
  fi
}
if [[ $1 -eq 0 ]]; then
	echo "Error no arugments provided"
	echo -e "enter what is transmited:\n\r1:hello world \n\r2:text file \n\r3:csv file\n\r4:PNG\n\r"
	exit 1
fi
# Call the is_root function to verify permissions
is_root
sudo chmod g+rw /dev/ttyS0
#get current time
current_time=$(date +%H:%M)
current_hour=$(echo $current_time | cut -d: -f 1)
previous_hour=$((current_hour-1))
while [ $current_time != "12:00" ]&&[ $current_time != "9:00" ]; do
  if [ $current_time == "$current_hour:00" ]; then
    # python Documents/Github/meshnetwork_in_forest/main/main.py $1
    python main/main.py $1
    echo "file ran successfully"
  fi
  break #becuase everyone needs a break sometime 
done