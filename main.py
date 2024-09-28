import os
import json

# Define the directory containing your JSON files
json_directory = 'json'  # Make sure this folder is in the same directory as your script
output_file = 'extracted_hrefs.json'  # Output file to save the extracted hrefs

# Initialize a set to store unique hrefs
all_hrefs = set()
processed_files = []

def extract_hrefs(data):
    """Recursively extract hrefs from the JSON data."""
    if isinstance(data, dict):  # If data is a dictionary
        for key, value in data.items():
            if key == 'href' and isinstance(value, str):  # If the key is 'href'
                all_hrefs.add(value)  # Add href to the set for uniqueness
            else:
                extract_hrefs(value)  # Recursively search in values
    elif isinstance(data, list):  # If data is a list
        for item in data:
            extract_hrefs(item)  # Recursively search in items

# Loop through each file in the specified directory
for filename in os.listdir(json_directory):
    if filename.endswith('.json'):  # Process only JSON files
        file_path = os.path.join(json_directory, filename)
        
        # Open and read the JSON file
        try:
            print(f"Processing file: {file_path}")  # Log the current file being processed
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)  # Load the JSON data
                extract_hrefs(data)  # Extract hrefs from the loaded JSON data
                processed_files.append(filename)  # Keep track of processed files

        except json.JSONDecodeError:
            print(f"Error decoding JSON from file: {file_path}")
        except Exception as e:
            print(f"An error occurred while processing {file_path}: {e}")

# Write all extracted unique hrefs to an output JSON file
with open(output_file, 'w', encoding='utf-8') as output:
    json.dump(list(all_hrefs), output, indent=4)  # Convert set to list before writing to JSON

print(f"Processed files: {processed_files}")
print(f"Extracted {len(all_hrefs)} unique hrefs to {output_file}")
