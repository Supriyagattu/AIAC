def generate_squares(n):
    """Generate a list of squares from 1 to n (inclusive) efficiently.

    Args:
        n (int): The upper limit of the range (inclusive).

    Returns:
        list: A list containing the squares of numbers from 1 to n.

    Example:
        >>> generate_squares(5)
        [1, 4, 9, 16, 25]
    """
    return [i ** 2 for i in range(1, n + 1)]

squares = generate_squares(999999)
print(len(squares))
