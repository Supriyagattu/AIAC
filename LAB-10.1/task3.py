def calculate_percentage(amount, percentage):
    """Calculate the percentage value of a given amount.

    Args:
        amount (float or int): The base amount.
        percentage (float or int): The percentage to calculate.

    Returns:
        float: The calculated percentage of the amount.
    """
    return amount * percentage / 100  # Perform percentage calculation

base_amount = 200  # The base value to calculate percentage from
percentage_value = 15  # The percentage to be calculated

# Print the result of the percentage calculation
print(calculate_percentage(base_amount, percentage_value))
