import json

# Load the first JSON file
with open('merged5.json', 'r', encoding='utf-8') as f1:
    data1 = json.load(f1)

# Load the second JSON file
with open('merged6.json', 'r', encoding='utf-8') as f2:
    data2 = json.load(f2)

# Merge the two JSON objects
# Merge the two JSON lists
if isinstance(data1, list) and isinstance(data2, list):
    merged_data = data1 + data2
else:
    raise ValueError("Both JSON files must contain lists to merge.")

# Save the merged JSON into a new file
with open('merged7.json', 'w', encoding='utf-8') as outfile:
    json.dump(merged_data, outfile, ensure_ascii=False, indent=4)
print("JSON files merged successfully!")
