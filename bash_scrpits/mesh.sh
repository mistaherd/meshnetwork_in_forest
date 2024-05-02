# !/bin/bash
# we are looking comand that will set what we are tranmsiting we dont care about reciver
if [ "$1" == "-t" ]; then
    if [-z "$2"]; then
        echo "Error: Please provide a file extension to tranmit"
    else
        echo "$2"
    fi
elif ["$1"=="-r"]; then
    echo "1"
else
    echo "Usage: -t <file extension> \n Usage: -r"  
fi