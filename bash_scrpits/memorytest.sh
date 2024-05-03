#!/bin/bash

dir_name=$(pwd)

size=$(du -sh "$dir_name" | cut -f1)

echo "$size"
 
