# !/bin/bash
timestamp=$(date +"%Y-%m-%d %H:%M:%S")
fname="camera_output_$timestamp.png"
output_dir="Images_camera"
if [ ! -d "$output_dir" ]; then
  # Create the directory if it doesn't exist
  mkdir -p "$output_dir"
  echo "Created directory: $output_dir"
fi
echo "$timestamp"