#!/bin/bash
echo "The current processes are as follows: "
# use ps too show the processes in the bakcgrond -e flag displays everything f will fromat the output into colums
ps -ef
# next we use check our memory
echo "memory useage: "
free -h
# next we check our services
echo "Current services"
systemctl --type=service
