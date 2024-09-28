from typing import List, Dict, Any, Set
import os
import json

# Define the directory containing your JSON files
json_directory = 'json'  # Make sure this folder is in the same directory as your script
output_file = 'extracted_hrefs.json'  # Output file to save the extracted hrefs

def extract_hrefs(data, all_hrefs: Set[str]):
    """Recursively extract hrefs from the JSON data."""
    if isinstance(data, dict):  # If data is a dictionary
        for key, value in data.items():
            if key == 'href' and isinstance(value, str):  # If the key is 'href'
                all_hrefs.add(value)  # Add href to the set for uniqueness
            else:
                extract_hrefs(value, all_hrefs)  # Recursively search in values
    elif isinstance(data, list):  # If data is a list
        for item in data:
            extract_hrefs(item, all_hrefs)  # Recursively search in items


def get_links(data: Dict[Any, Any]) -> List[str]:
    # Initialize a set to store unique hrefs
    all_hrefs = set()
    processed_files = []

    for filename in os.listdir(json_directory):
        if filename.endswith('.json'):  # Process only JSON files
            file_path = os.path.join(json_directory, filename)
            
            # Open and read the JSON file
            try:
                print(f"Processing file: {file_path}")  # Log the current file being processed
                with open(file_path, 'r', encoding='utf-8') as file:
                    data = json.load(file)  # Load the JSON data
                    extract_hrefs(data, all_hrefs)  # Extract hrefs from the loaded JSON data
                    processed_files.append(filename)  # Keep track of processed files

            except json.JSONDecodeError:
                print(f"Error decoding JSON from file: {file_path}")
            except Exception as e:
                print(f"An error occurred while processing {file_path}: {e}")

    # Write all extracted unique hrefs to an output JSON file
    # with open(output_file, 'w', encoding='utf-8') as output:
    #     json.dump(list(all_hrefs), output, indent=4)  # Convert set to list before writing to JSON

    # print(f"Processed files: {processed_files}")
    # print(f"Extracted {len(all_hrefs)} unique hrefs to {output_file}")

    return all_hrefs

if __name__ == "__main__":
    print(get_links(dict()))