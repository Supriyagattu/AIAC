def grade(score):
    """
    Return the letter grade for a given numeric score.

    Args:
        score (int or float): The score to grade. Should be between 0 and 100.

    Returns:
        str: The letter grade ("A", "B", "C", "D", or "F").

    Raises:
        TypeError: If score is not a number.
        ValueError: If score is not between 0 and 100.
    """
    if not isinstance(score, (int, float)):
        raise TypeError("Score must be a number.")
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100.")

    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Example usage:
if __name__ == "__main__":
    test_scores = [95, 82, 76, 64, 58, 101, -5, "A"]
    for s in test_scores:
        try:
            print(f"Score: {s} => Grade: {grade(s)}")
        except Exception as e:
            print(f"Score: {s} => Error: {e}")






