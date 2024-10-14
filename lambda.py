# Lambda function to check if a number is odd or even
check_odd_even = lambda x: f"{x} is even." if x % 2 == 0 else f"{x} is odd."

# Example usage
num = int(input("Enter a number: "))
print(check_odd_even(num))
