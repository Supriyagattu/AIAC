# Using for loop
def print_multiples_for(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

# Using while loop
def print_multiples_while(num):
    i = 1
    while i <= 10:
        print(f"{num} x {i} = {num * i}")
        i += 1

# Example usage:
if __name__ == "__main__":
    print("Multiples using for loop:")
    print_multiples_for(5)
    print("\nMultiples using while loop:")
    print_multiples_while(7)