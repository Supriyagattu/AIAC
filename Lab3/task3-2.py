def calculate_power_bill(units, customer_type):
    """
    Calculates the power bill for a given number of units and customer type.
    The billing is based on the following slab rates for each customer type:

    For 'residential':
      - First 100 units: Rs. 5 per unit
      - Next 100 units (101-200): Rs. 7 per unit
      - Above 200 units: Rs. 10 per unit

    For 'commercial':
      - First 100 units: Rs. 8 per unit
      - Next 100 units (101-200): Rs. 10 per unit
      - Above 200 units: Rs. 15 per unit

    For 'industrial':
      - First 100 units: Rs. 10 per unit
      - Next 100 units (101-200): Rs. 15 per unit
      - Above 200 units: Rs. 20 per unit

    Parameters:
    units (int or float): The number of units consumed.
    customer_type (str): Type of customer ('residential', 'commercial', 'industrial').

    Returns:
    float: The total power bill.
    """
    if units < 0:
        raise ValueError("Number of units cannot be negative.")

    customer_type = customer_type.lower()
    if customer_type == 'residential':
        rates = [5, 7, 10]
    elif customer_type == 'commercial':
        rates = [8, 10, 15]
    elif customer_type == 'industrial':
        rates = [10, 15, 20]
    else:
        raise ValueError("Invalid customer type. Choose 'residential', 'commercial', or 'industrial'.")

    bill = 0
    if units <= 100:
        bill = units * rates[0]
    elif units <= 200:
        bill = 100 * rates[0] + (units - 100) * rates[1]
    else:
        bill = 100 * rates[0] + 100 * rates[1] + (units - 200) * rates[2]
    return bill

# Example usage:
if __name__ == "__main__":
    try:
        units = float(input("Enter the number of units consumed: "))
        customer_type = input("Enter customer type (residential/commercial/industrial): ")
        total_bill = calculate_power_bill(units, customer_type)
        print(f"Total power bill for {units} units ({customer_type}) is: Rs. {total_bill:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
