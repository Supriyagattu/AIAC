
def convert_temperature(value, from_unit, to_unit):
    """
    Converts temperature between Celsius, Fahrenheit, Kelvin, and Reaumur.

    Parameters:
    value (float): The temperature value to convert.
    from_unit (str): The unit of the input temperature ('C', 'F', 'K', or 'R').
    to_unit (str): The unit to convert to ('C', 'F', 'K', or 'R').

    Returns:
    float: The converted temperature value.

    Raises:
    ValueError: If an invalid unit is provided.
    """
    from_unit = from_unit.upper()
    to_unit = to_unit.upper()

    if from_unit == to_unit:
        return value

    # Convert input to Celsius first
    if from_unit == 'C':
        celsius = value
    elif from_unit == 'F':
        celsius = (value - 32) * 5/9
    elif from_unit == 'K':
        celsius = value - 273.15
    elif from_unit == 'R':
        celsius = value * 5/4
    else:
        raise ValueError("Invalid from_unit. Use 'C', 'F', 'K', or 'R'.")

    # Convert from Celsius to target unit
    if to_unit == 'C':
        return celsius
    elif to_unit == 'F':
        return celsius * 9/5 + 32
    elif to_unit == 'K':
        return celsius + 273.15
    elif to_unit == 'R':
        return celsius * 4/5
    else:
        raise ValueError("Invalid to_unit. Use 'C', 'F', 'K', or 'R'.")

if __name__ == "__main__":
    print("Temperature Converter")
    print("Supported units: Celsius (C), Fahrenheit (F), Kelvin (K), Reaumur (R)")
    try:
        value = float(input("Enter the temperature value to convert: "))
        from_unit = input("Enter the unit to convert from (C/F/K/R): ").strip().upper()
        to_unit = input("Enter the unit to convert to (C/F/K/R): ").strip().upper()
        result = convert_temperature(value, from_unit, to_unit)
        print(f"{value}°{from_unit} is equal to {result:.2f}°{to_unit}")
    except ValueError as e:
        print(f"Error: {e}")
