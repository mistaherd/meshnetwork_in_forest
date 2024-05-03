#!/bin/bash
is_root() {
  if [[$EUID -ne 0 ]]; then
    echo "This script requires root privileges. Please run with sudo."
    exit 1
  fi
}

# Call the is_root function to verify permissions
is_root
sudo chmod g+rw /dev/ttyS0
#get current time
current_time=$(date +%H:%M)
current_hour=$(echo $current_time | cut -d: -f 1)
previous_hour=$((current_hour-1))
while [$"current_hour" != "12:00" ]&&[$"current_hour" != "09:00" ]; do
  if [$"current_hour" -eq $((previous_hour+1)) ]; then
    # python /home/mistaherd/Documents/Github/meshnetwork_in_forest/main/main.py
    python main/main.py
    echo "file ran successfully"
  fi
  # break #becuase everyone needs a break sometime 
done

