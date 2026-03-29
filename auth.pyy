import json
import os
import hashlib

DATA_FILE = "data/users.json"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    os.makedirs("data", exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(users, f, indent=4)

def create_account(username, password):
    users = load_users()
    if username in users:
        return False, "Username already exists."
    users[username] = hash_password(password)
    save_users(users)
    return True, "Account created successfully."

def login_user(username, password):
    users = load_users()
    if username in users and users[username] == hash_password(password):
        return True
    return False