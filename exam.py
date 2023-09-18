def calculate_average(numbers):
    if not numbers:
        return 0  # Avoid division by zero for an empty list
    total = sum(numbers)
    return total / len(numbers)
numbers = [2, 5]
average = calculate_average(numbers)
print(f"The average is: {average}")