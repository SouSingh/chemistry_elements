import json

# Read the original JSON data from a file
with open("chemical.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Convert to desired format
converted_data = []

for item in data:
    # Get the "Name" field (first value)
    input_item = list(item.values())[0]

    # Extract the remaining key-value pairs
    output_items = {key: value for key, value in item.items() if key != "Name"}

    # Create a string representation of the remaining key-value pairs
    import itertools
    output_string = ([f"{key}: {value}" for key, value in itertools.islice(output_items.items(), 12)])


    # Append the converted item to the list
    converted_data.append({
        "input": input_item,
        "output": output_string
    })

# Save the converted data to a new JSON file
with open("converted_chemical_properties1.json", "w", encoding="utf-8") as file:
    json.dump(converted_data, file, ensure_ascii=False, indent=4)

# Print the converted data for verification
print(json.dumps(converted_data, ensure_ascii=False, indent=4))
