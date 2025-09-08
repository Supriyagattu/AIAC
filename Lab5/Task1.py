import hashlib
import getpass
import os
import json

# File to store user credentials securely (hashed passwords)
USER_DB_FILE = 'users_db.json'

def hash_password(password):
    """Hash a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    """Load users from the database file."""
    if not os.path.exists(USER_DB_FILE):
        return {}
    with open(USER_DB_FILE, 'r') as f:
        return json.load(f)

def save_users(users):
    """Save users to the database file."""
    with open(USER_DB_FILE, 'w') as f:
        json.dump(users, f)

def register():
    """Register a new user with username and password."""
    users = load_users()
    username = input("Enter new username: ")
    if username in users:
        print("Username already exists.")
        return
    password = getpass.getpass("Enter new password: ")
    # Store only the hashed password, not plain-text
    users[username] = hash_password(password)
    save_users(users)
    print("Registration successful.")

def login():
    """Login an existing user."""
    users = load_users()
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    hashed = hash_password(password)
    # Compare hashed password, not plain-text
    if users.get(username) == hashed:
        print("Login successful.")
    else:
        print("Invalid username or password.")

def main():
    """Main function to choose register or login."""
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

# --- Security Review ---
# - No hardcoded passwords.
# - Passwords are not stored in plain-text; they are hashed using SHA-256.
# - No encryption for the user database file, but passwords are not readable.
# - For production, use salted hashes (e.g., bcrypt) and secure storage.