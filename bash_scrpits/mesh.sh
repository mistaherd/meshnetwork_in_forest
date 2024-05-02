# !/bin/bash
# we are looking comand that will set what we are tranmsiting we dont care about reciver
if [ "$1" == "listen" ]; then
    if [-z "$2"]; then
        echo "Error: Please provide a file extension to tranmit"
    else
        echo "$2"
    fi
else
    echo "Usage: mesh -t <file extension>"
fi