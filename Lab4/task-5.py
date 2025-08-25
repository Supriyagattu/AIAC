# INSERT_YOUR_CODE
def most_frequent_word(paragraph):
    """
    Converts the paragraph to lowercase, removes punctuation,
    and returns the most frequently used word.
    """
    # Convert to lowercase
    text = paragraph.lower()
    # Remove punctuation
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    text = ''.join(char for char in text if char not in punctuation)
    # Split into words
    words = text.split()
    if not words:
        return None
    # Count word frequencies
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    # Find the most frequent word
    most_frequent = max(freq, key=freq.get)
    return most_frequent
    # INSERT_YOUR_CODE
if __name__ == "__main__":
    paragraph = input("Enter a paragraph: ")
    result = most_frequent_word(paragraph)
    if result:
        print(f"The most frequent word is: '{result}'")
    else:
        print("No words found in the input.")
        # INSERT_YOUR_CODE
        # Example 1: Function that converts text to lowercase and returns its length
        def lowercase_and_length(text):
            """
            Converts the input text to lowercase and returns its length.
            """
            lower_text = text.lower()
            return len(lower_text)

        # Example 2: Function that reverses a string
        def reverse_string(s):
            """
            Reverses the input string and returns it.
            """
            return s[::-1]

        # Example 3: Function that removes spaces from a sentence
        def remove_spaces(sentence):
            """
            Removes all spaces from the input sentence and returns the result.
            """
            return sentence.replace(' ', '')

        # Ask the user for these as well
        user_text = input("Enter text for lowercase and length: ")
        print(f"Lowercase text length: {lowercase_and_length(user_text)}")

        user_string = input("Enter a string to reverse: ")
        print(f"Reversed string: {reverse_string(user_string)}")

        user_sentence = input("Enter a sentence to remove spaces: ")
        print(f"Sentence without spaces: {remove_spaces(user_sentence)}")
        # INSERT_YOUR_CODE
        # Example 1: Function that converts text to lowercase and returns its length
        def lowercase_and_length(text):
            """
            Converts the input text to lowercase and returns its length.
            """
            lower_text = text.lower()
            return len(lower_text)

        # Example 2: Function that reverses a string
        def reverse_string(s):
            """
            Reverses the input string and returns it.
            """
            return s[::-1]

        # Example 3: Function that removes spaces from a sentence
        def remove_spaces(sentence):
            """
            Removes all spaces from the input sentence and returns the result.
            """
            return sentence.replace(' ', '')

        # Use the entered paragraph for all three examples
        print(f"Example 1: Lowercase text length: {lowercase_and_length(paragraph)}")
        print(f"Example 2: Reversed string: {reverse_string(paragraph)}")
        print(f"Example 3: Sentence without spaces: {remove_spaces(paragraph)}")
