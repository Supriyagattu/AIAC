users_db = {}

def register_user(username, password):
    """
    Registers a new user with the given username and password.
    Returns True if registration is successful, False if username already exists.
    """
    if username in users_db:
        return False  # Username already exists
    users_db[username] = password
    return True

def login_user(username, password):
    """
    Logs in an existing user by checking the username and password.
    Returns True if login is successful, False otherwise.
    """
    if username in users_db and users_db[username] == password:
        return True
    return False

if __name__ == "__main__":
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Enter your choice (1/2/3): ").strip()
        if choice == '1':
            username = input("Enter new username: ").strip()
            password = input("Enter new password: ").strip()
            if register_user(username, password):
                print("Registration successful!")
            else:
                print("Username already exists. Please try a different username.")
        elif choice == '2':
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()
            if login_user(username, password):
                print("Login successful!")
            else:
                print("Invalid username or password.")
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
