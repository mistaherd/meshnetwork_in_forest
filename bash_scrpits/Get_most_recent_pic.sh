#!/bin/bash
lastest_file=$(ls ../data_storage/Images |grep -Po 'camera_output_\d{4}-\d{2}-\d{2}_\d{2}_\d{2}_\d{2}\.png' | sort | tail -n 1)
echo  "$lastest_file"
