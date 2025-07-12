# This program generates a Fibonacci sequence up to a number entered by the user

# Ask the user how many numbers they want in the Fibonacci series
count = int(input("Enter how many Fibonacci numbers you want: "))

# First two numbers of the Fibonacci sequence
num1 = 0
num2 = 1

# List to store the sequence
fib_series = []

# Use a loop to generate the series
for i in range(count):
    fib_series.append(num1)
    # Update numbers: next = num1 + num2
    next_num = num1 + num2
    num1 = num2
    num2 = next_num

# Print the result
print("Fibonacci sequence:", fib_series)
