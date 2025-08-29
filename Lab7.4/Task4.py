def compute_ratios(values):
    results = []
    for i in range(len(values)):
        for j in range(i, len(values)):
            try:
                ratio = values[i] / (values[j] - values[i])
                results.append((i, j, ratio))
            except ZeroDivisionError:
                print(f"Error: Division by zero when i={i}, j={j}, values[i]={values[i]}, values[j]={values[j]}")
    return results

# Example input
nums = [5, 10, 15, 20, 25]

# Function call and output
print(compute_ratios(nums))