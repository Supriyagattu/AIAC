
def area_of_rectangle(length, breadth):
    """Calculate the area of a rectangle.

    Args:
        length (float): The length of the rectangle. Must be positive.
        breadth (float): The breadth of the rectangle. Must be positive.

    Returns:
        float: The area of the rectangle.

    Raises:
        ValueError: If length or breadth is not positive.
        TypeError: If length or breadth is not a number.
    """
    if not isinstance(length, (int, float)) or not isinstance(breadth, (int, float)):
        raise TypeError("Length and breadth must be numbers.")
    if length <= 0 or breadth <= 0:
        raise ValueError("Length and breadth must be positive values.")
    return length * breadth


def main():
    """Prompt user for rectangle dimensions and display the area."""
    try:
        
        length = float(input("Enter the length of the rectangle: "))
        breadth = float(input("Enter the breadth of the rectangle: "))
        area = area_of_rectangle(length, breadth)
        print(f"The area of the rectangle is {area}")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()


