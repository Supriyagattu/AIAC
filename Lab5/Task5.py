def greet_user(name, gender):
    if gender.lower() == "male":
        title = "Mr."
    else:
        title = "Mrs."
    return f"Hello, {title} {name}! Welcome."


# Example usage:
if __name__ == "__main__":
    name = input("Enter your name: ")
    gender = input("Enter your gender (male/female): ")