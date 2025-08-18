def calculate_electricity_bill(units):
    """
    Calculates the electricity bill based on a flat rate of $0.15 per unit.

    Parameters:
    units (int or float): The number of units consumed.

    Returns:
    float: The total bill amount.
    """
    if units < 0:
        raise ValueError("Number of units cannot be negative.")
    rate_per_unit = 0.15
    return units * rate_per_unit

if __name__ == "__main__":
    try:
        units = float(input("Enter the number of units consumed: "))
        total_bill = calculate_electricity_bill(units)
        print(f"Total electricity bill for {units} units is: ${total_bill:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
