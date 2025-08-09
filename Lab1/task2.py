def fibonacci_sequence(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

if __name__ == "__main__":
    n = int(input("Enter the number of terms: "))
    result = fibonacci_sequence(n)
    print("Fibonacci sequence up to", n, "terms:")
    print(result)
