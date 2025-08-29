def sort_list(data):
    numbers = sorted([x for x in data if isinstance(x, (int, float))])
    strings = sorted([x for x in data if isinstance(x, str)])
    return numbers + strings

items = [3, "apple", 1, "banana", 2]
print(sort_list(items))
