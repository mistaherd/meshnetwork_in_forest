import glob
search_pattern="sensor_data.csv"
# Use glob to find all matching files
files = glob.glob(search_pattern)
# Check if any files were found
if files:
  print("Found CSV files:", files)
else:
  print("No files found matching", search_pattern)

  