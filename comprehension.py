# Function to check odd or even using list comprehension
def check_numbers_with_comprehension(numbers):
    return [f"{num} is even." if num % 2 == 0 else f"{num} is odd." for num in numbers]

# Example usage
num_list = [10, 15, 22, 33, 44]
results = check_numbers_with_comprehension(num_list)
print("\n".join(results))
