def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    s = input("Enter a string: ")
    if is_palindrome(s):
        print("Valid palindrome")
    else:
        print("Not palindrome")