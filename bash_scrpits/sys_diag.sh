#!/bin/bash
echo "The current processes are as follows: ">../data_storage/sys_dia.txt
ps -ef>>../data_storage/sys_dia.txt
# next we use check our memory
echo "memory useage: ">>../data_storage/sys_dia.txt
free -h >>../data_storage/sys_dia.txt
# next we check our services
echo "Current services">>../data_storage/sys_dia.txt

systemctl --type=service >>../data_storage/sys_dia.txt
