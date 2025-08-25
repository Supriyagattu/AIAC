# INSERT_YOUR_CODE
def analyze_csv_file(file_path):
    """
    Opens a CSV file and returns:
    - Number of rows
    - Number of empty rows
    - Number of words in the file
    
    Returns:
        tuple: (total_rows, empty_rows, word_count)
    """
    import csv

    total_rows = 0
    empty_rows = 0
    word_count = 0

    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            total_rows += 1
            # A row is empty if all its cells are empty or whitespace
            if all(cell.strip() == '' for cell in row):
                empty_rows += 1
            # Count words in all cells of the row
            for cell in row:
                word_count += len(cell.strip().split())

    return total_rows, empty_rows, word_count

# Example usage and testing
if __name__ == "__main__":
    # Test with the SRU.csv.txt file in your workspace
    try:
        total_rows, empty_rows, word_count = analyze_csv_file("SRU.csv.txt")
        print(f"Total rows: {total_rows}")
        print(f"Empty rows: {empty_rows}")
        print(f"Total words: {word_count}")
    except FileNotFoundError:
        print("SRU.csv.txt not found. Please make sure the file exists in the current directory.")
    except Exception as e:
        print(f"Error reading file: {e}")
