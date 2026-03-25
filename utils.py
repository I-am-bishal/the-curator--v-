# utils.py

import json

# Load data from JSON file
def load_data(file):
    try:
        with open(file, "r") as f:
            return json.load(f)
    except:
        return []

# Save data to JSON file
def save_data(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=4)