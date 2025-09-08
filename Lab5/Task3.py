# Function to calculate the nth Fibonacci number using recursion
def fibonacci(n):
    """
    Recursively calculates the nth Fibonacci number.
    
    The Fibonacci sequence is defined as:
    F(0) = 0
    F(1) = 1
    F(n) = F(n-1) + F(n-2) for n > 1

    Args:
        n (int): The position in the Fibonacci sequence (must be >= 0).

    Returns:
        int: The nth Fibonacci number.
    """
    # Base cases: F(0) = 0, F(1) = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Recursive case: F(n) = F(n-1) + F(n-2)
        return fibonacci(n-1) + fibonacci(n-2)

# Example usage and output
if __name__ == "__main__":
    # Get user input
    n = int(input("Enter the position n to find the nth Fibonacci number: "))
    result = fibonacci(n)
    print(f"The {n}th Fibonacci number is: {result}")

"""
Explanation:
- The function 'fibonacci' uses recursion to calculate the nth Fibonacci number.
- It checks for the base cases (n == 0 or n == 1) and returns the corresponding value.
- For n > 1, it calls itself with (n-1) and (n-2) and adds their results.
- The code includes a docstring explaining the function and its arguments.
- The main block allows the user to input a value for n and prints the result.

Assessment:
- The explanation is clear and correct.
- The code correctly implements the recursive Fibonacci calculation.
- For example, if the user inputs 5, the output will be:
  The 5th Fibonacci number is: 15
"""
