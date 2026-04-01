import json
import os
import numpy as np


DATA_FILE = "data/user_records.json"


def convert_numpy(obj):
    """
    Convert NumPy/Pandas types into normal Python types
    """
    if isinstance(obj, np.integer):
        return int(obj)

    elif isinstance(obj, np.floating):
        return float(obj)

    elif isinstance(obj, np.ndarray):
        return obj.tolist()

    elif isinstance(obj, np.bool_):
        return bool(obj)

    return obj


def load_user_records():
    """
    Load all user records
    """
    if not os.path.exists(DATA_FILE):
        return {}

    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}


def save_user_records(data):
    """
    Save all user records
    """
    os.makedirs("data", exist_ok=True)

    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4, default=convert_numpy)


def append_user_record(username, record):
    """
    Add a new record for user
    """
    data = load_user_records()

    if username not in data:
        data[username] = []

    clean_record = json.loads(json.dumps(record, default=convert_numpy))
    data[username].append(clean_record)

    save_user_records(data)


def get_user_records(username):
    """
    Get all records of a user
    """
    data = load_user_records()
    return data.get(username, [])


# ✅ Compatibility function for old app.py
def get_user_history(username):
    """
    Backward-compatible alias for old code
    """
    return get_user_records(username)