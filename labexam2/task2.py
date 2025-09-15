def validate_payment(card, exp, cvv):
    """
    Validates payment information.

    Parameters:
        card (str): Card number as a string. Must be 16 digits.
        exp (str): Expiry date in MM/YY format.
        cvv (int or str): CVV code. Must be 3 digits.

    Returns:
        bool: True if card number is 16 digits and CVV is 3 digits, False otherwise.
    """
    # Check if card number is 16 digits and CVV is 3 digits
    if len(card) == 16 and len(str(cvv)) == 3:
        return True
    else:
        return False

# Sample Input
result = validate_payment("1234567890123456", "12/25", 123)
print(result)  # Sample Output: True

