def sort_list(arr):
    """
    Sorts a list of numbers in ascending order using the bubble sort algorithm.

    Parameters:
    arr (list): The list of numbers to sort.

    Returns:
    list: A new sorted list.
    """
    n = len(arr)
    sorted_arr = arr.copy()
    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
    return sorted_arr

if __name__ == "__main__":
    user_input = input("Enter numbers separated by spaces: ")
    try:
        numbers = [int(x) for x in user_input.strip().split()]
        print("Original list:", numbers)
        print("Sorted list:", sort_list(numbers))
    except ValueError:
        print("Please enter only integers separated by spaces.")
