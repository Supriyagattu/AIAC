def count_lines(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Static file path
file_path = "example_task.txt" 


# Call the function and print the result
line_count = count_lines(file_path)
print(f"The file '{file_path}' has {line_count} lines.")