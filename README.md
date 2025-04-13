task 1

Define the factorial function
def factorial(n): # Initialize the result variable result = 1

# Loop to calculate the factorial
for i in range(1, n + 1):
    result *= i  # Multiply result by each number from 1 to n

return result
Call the function with a sample number (e.g., 5)
sample_number = 5 result = factorial(sample_number)

Print the result
print(f"The factorial of {sample_number} is: {result}")


task 2

import math

Ask the user for a number
num = float(input("Enter a number: "))

Calculate the square root, natural logarithm, and sine of the number
sqrt_value = math.sqrt(num) log_value = math.log(num) # Natural logarithm (log base e) sin_value = math.sin(num) # Sine of the number in radians

Display the results
print(f"The square root of {num} is: {sqrt_value}") print(f"The natural logarithm (log base e) of {num} is: {log_value}") print(f"The sine of {num} (in radians) is: {sin_value}")
