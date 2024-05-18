#!/bin/bash
timestamp=$(date +"%Y-%m-%d_%H_%M_%S")
fname="camera_output_$timestamp.png"
output_dir="Images_camera"
if [ ! -d "$output_dir" ]; then
  # Create the directory if it doesn't exist
  mkdir -p "$output_dir"
fi
rpicam-still --raw -o "$output_dir/$fname"