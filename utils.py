import json
import os

DATA_FILE = "data/user_data.json"

def append_user_record(username, record):
    """Append a record for a specific username"""
    os.makedirs("data", exist_ok=True)
    data = {}
    
    # Check if file exists and is not empty
    if os.path.exists(DATA_FILE) and os.path.getsize(DATA_FILE) > 0:
        with open(DATA_FILE, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = {}  # If file is corrupted or empty, start fresh
    
    if username not in data:
        data[username] = []
    data[username].append(record)
    
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def get_user_history(username):
    """Get all records for a specific username"""
    if os.path.exists(DATA_FILE) and os.path.getsize(DATA_FILE) > 0:
        with open(DATA_FILE, "r") as f:
            try:
                data = json.load(f)
                return data.get(username, [])
            except json.JSONDecodeError:
                return []
    return []