import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    data = []

    # Read CSV file
    with open(csv_file_path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)

    # Write to JSON file
    with open(json_file_path, mode='w') as json_file:
        json.dump(data, json_file, indent=4)

# Example usage
csv_file_path = 'elementdatavalues.csv'
json_file_path = 'chemical1.json'
csv_to_json(csv_file_path, json_file_path)
