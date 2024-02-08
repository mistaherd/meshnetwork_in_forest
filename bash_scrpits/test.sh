# !/bin/bash

dir_name=$0

size=$(du -sh "$dir_name" | cut -f1)

echo "$size"
 
