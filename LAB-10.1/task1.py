def calc_average(marks):
    """Calculate the average score from a list of marks.

    Args:
        marks (list of float or int): List containing the marks of a student.

    Returns:
        float: The average score.

    Raises:
        ValueError: If marks list is empty.
        TypeError: If marks is not a list or contains non-numeric values.
    """
    if not isinstance(marks, list):
        raise TypeError("marks must be a list.")
    if not marks:
        raise ValueError("marks list cannot be empty.")
    for m in marks:
        if not isinstance(m, (int, float)):
            raise TypeError("All elements in marks must be numbers.")
    total = 0
    for m in marks:
        total += m
    average = total / len(marks)
    return average

if __name__ == "__main__":
    marks = [85, 90, 78, 92]
    print("Average Score is", calc_average(marks))
