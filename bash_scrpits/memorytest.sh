# !/bin/bash

dir_name=$1

size=$(du -sh "$dir_name" | cut -f1)

echo "$size"
 
