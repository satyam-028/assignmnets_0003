import math

# Ask the user for a number
num = float(input("Enter a number: "))

# Calculate the square root, natural logarithm, and sine of the number
sqrt_value = math.sqrt(num)
log_value = math.log(num)  # Natural logarithm (log base e)
sin_value = math.sin(num)  # Sine of the number in radians

# Display the results
print(f"The square root of {num} is: {sqrt_value}")
print(f"The natural logarithm (log base e) of {num} is: {log_value}")
print(f"The sine of {num} (in radians) is: {sin_value}")