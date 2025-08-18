users_db = {}

def register_user(username, password):
    """
    Registers a new user with the given username and password.
    Returns True if registration is successful, False if username already exists.
    """
    if username in users_db:
        return False
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

