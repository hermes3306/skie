#!/bin/bash

# Define the directory containing CSV files
csv_directory="."

# Loop through each CSV file in the directory
for file in "$csv_directory"/*.csv; do
    # Check if the file exists and is a regular file
    if [ -f "$file" ]; then
        echo "Processing $file..."
        # Replace single quotes with \'
        python3 -c "
import csv

file_path = '$file'

# Function to replace ' with \'
def replace_quotes(csv_file):
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        data = list(reader)
    with open(csv_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow([cell.replace(\"'\", \"\\\\'\") for cell in row])

replace_quotes(file_path)
"
        echo "Replacement done for $file"
    else
        echo "$file is not a regular file."
    fi
done

echo "All CSV files processed."

