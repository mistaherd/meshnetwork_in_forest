#!/bin/bash
sudo chmod 666 /dev/ttyS0
if [[ "$1" =='1']]; then
	python test_tranmiter.py
elif [["$1"=='0']]; then
	python test_reciver.py
else
	echo "this need a 1 or 0"
fi
