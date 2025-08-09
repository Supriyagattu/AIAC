def reverse_string(s):
    return s[::-1]

if __name__ == "__main__":
    input_str = input("Enter a string: ")
    print("Reversed string:", reverse_string(input_str))