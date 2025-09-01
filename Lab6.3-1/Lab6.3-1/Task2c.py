# Function to print multiples of a number using a for loop
def print_multiples_for(num):
    for i in range(1, 11):  # Loop from 1 to 10
        print(f"{num} x {i} = {num * i}")  # Print the multiplication result

# Function to print multiples of a number using a while loop
def print_multiples_while(num):
    i = 1  # Initialize counter
    while i <= 10:  # Loop until 10
        print(f"{num} x {i} = {num * i}")  # Print the multiplication result
        i += 1  # Increment counter

# Call the function to print multiples of 5 using for loop
print(print_multiples_for(5))
# Call the function to print multiples of 7 using while loop
print(print_multiples_while(7))
