# !/bin/bash
#activate meshnetwork_in_forest enviromnet file
enviromnet_dir=env/bin/activate
source $enviromnet_dir
#get current time
current_time=$(date +%H:%M)
current_hour=$(echo $current_time | cut -d: -f 1)
previous_hour=$((current_hour-1))
while [ "$current_hour" != "12:00" ]&&[ "$current_hour" != "09:00" ]; do
 
  if [ "$current_hour" = $(previous_hour+1) ]; then
    python main\main.py
  fi
  echo "file ran successfully"
done

