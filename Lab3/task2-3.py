def sort_list(arr, order='asc'):
    """
    Sorts a list of numbers or strings in ascending or descending order.

    Parameters:
    arr (list): The list of numbers or strings to sort.
    order (str): 'asc' for ascending, 'desc' for descending. Default is 'asc'.

    Returns:
    list: A new sorted list.
    """
    reverse = True if order == 'desc' else False
    try:
        return sorted(arr, reverse=reverse)
    except TypeError:
        # If mixed types, sort by string representation
        return sorted(arr, key=lambda x: str(x), reverse=reverse)

if __name__ == "__main__":
    user_input = input("Enter numbers or strings separated by spaces: ")
    arr = user_input.strip().split()
    order = input("Enter order ('asc' for ascending, 'desc' for descending): ").strip().lower()
    if order not in ['asc', 'desc']:
        print("Invalid order specified. Defaulting to ascending.")
        order = 'asc'
    # Try to convert to numbers if possible
    def try_convert(x):
        try:
            return int(x)
        except ValueError:
            try:
                return float(x)
            except ValueError:
                return x
    arr = [try_convert(x) for x in arr]
    print("Sorted list:", sort_list(arr, order))
