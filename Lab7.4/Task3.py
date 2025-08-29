# Assignment: AI Assisted Coding - File Handling Examples

# --- Code 1: Write "Hello, world!" to a file ---
def write_hello():
    with open("example.txt", "w") as f:
        f.write("Hello, world!")


# --- Code 2: Write to two separate files ---
def write_two_files():
    with open("data1.txt", "w") as f1, open("data2.txt", "w") as f2:
        f1.write("First file content\n")
        f2.write("Second file content\n")
    print("Files written successfully")


# --- Code 3: Read from input.txt and write uppercase to output.txt ---
def convert_to_uppercase():
    # Ensure input.txt exists
    try:
        with open("input.txt", "r") as input_file:
            data = input_file.readlines()
    except FileNotFoundError:
        # Create input.txt with sample content if not found
        with open("input.txt", "w") as f:
            f.write("hello world\nthis is ai lab\npython is fun\n")
        print("Created 'input.txt' with sample content.")
        with open("input.txt", "r") as input_file:
            data = input_file.readlines()

    with open("output.txt", "w") as output:
        for line in data:
            output.write(line.upper())

    print("Processing done")


# --- Code 4: Read numbers, square them, and write to squares.txt ---
def square_numbers():
    # Create numbers.txt if missing
    try:
        with open("numbers.txt", "r") as f:
            nums = f.readlines()
    except FileNotFoundError:
        with open("numbers.txt", "w") as f:
            f.write("2\n3\n5\n")
        print("Created 'numbers.txt' with sample numbers.")
        with open("numbers.txt", "r") as f:
            nums = f.readlines()

    squares = []
    for n in nums:
        n = n.strip()
        if n.isdigit():
            squares.append(int(n) * int(n))

    with open("squares.txt", "w") as f2:
        for sq in squares:
            f2.write(str(sq) + "\n")

    print("Squares written")


# --- Run All Functions ---
write_hello()
write_two_files()
convert_to_uppercase()
square_numbers()