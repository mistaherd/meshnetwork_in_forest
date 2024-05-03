# !/bin/bash
current_time=$(date +%H:%M)
current_hour=$(echo $current_time | cut -d: -f 1)
previous_hour=$((current_hour-1))
# echo "$previous_hour"
# if [["$current_hour" != "12:00" && "$current_hour" != "09:00" ]];then
#     echo test
# fi
echo "$current_hour" -n
eq "12:00" && "$current_hour" != "09:00" 