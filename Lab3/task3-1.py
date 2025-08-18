def calculate_power_bill(units):
    """
    Calculates the power bill for a given number of units.
    The billing is based on the following slab rates:
      - For first 100 units: Rs. 5 per unit
      - For next 100 units (101-200): Rs. 7 per unit
      - For units above 200: Rs. 10 per unit

    Parameters:
    units (int or float): The number of units consumed.

    Returns:
    float: The total power bill.
    """
    if units < 0:
        raise ValueError("Number of units cannot be negative.")

    bill = 0
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = 100 * 5 + (units - 100) * 7
    else:
        bill = 100 * 5 + 100 * 7 + (units - 200) * 10
    return bill

# Example usage:
if __name__ == "__main__":
    try:
        units = float(input("Enter the number of units consumed: "))
        total_bill = calculate_power_bill(units)
        print(f"Total power bill for {units} units is: Rs. {total_bill:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
