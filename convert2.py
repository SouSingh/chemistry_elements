import csv
import json

# Load data from JSON file with UTF-8 encoding
with open('merged7.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Write data to CSV file with UTF-8 encoding
with open('data.csv', 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    
    # Write the header
    writer.writerow(['input', 'output'])
    
    # Write the rows
    for item in data:
        writer.writerow([item['input'], item['output']])
