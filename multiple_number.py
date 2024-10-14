# Function to check if numbers in a list are odd or even
def check_multiple_numbers(numbers):
    results = []
    for number in numbers:
        if number % 2 == 0:
            results.append(f"{number} is even.")
        else:
            results.append(f"{number} is odd.")
    return results

# Example usage
num_list = [1, 2, 3, 4, 5, 6]
results = check_multiple_numbers(num_list)
for result in results:
    print(result)
