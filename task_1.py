# Define the factorial function
def factorial(n):
    # Initialize the result variable
    result = 1
    
    # Loop to calculate the factorial
    for i in range(1, n + 1):
        result *= i  # Multiply result by each number from 1 to n
    
    return result

# Call the function with a sample number (e.g., 5)
sample_number = 5
result = factorial(sample_number)

# Print the result
print(f"The factorial of {sample_number} is: {result}")