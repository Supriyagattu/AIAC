def is_valid_indian_mobile(number: str) -> bool:
    """
    Validates an Indian mobile number.
    The number must start with 6, 7, 8, or 9 and contain exactly 10 digits.
    """
    return number.isdigit() and len(number) == 10 and number[0] in {'6', '7', '8', '9'}

# Example usage:
user_input = input("Enter an Indian mobile number: ")
if is_valid_indian_mobile(user_input):
    print("Valid Indian mobile number.")
else:
    print("Invalid Indian mobile number.")