# This is a simple calculator for basic arithmetic operations

print("Simple Calculator")
print("Choose operation:")
print("A. Addition")
print("B. Subtraction")
print("C. Multiplication")
print("D. Division")

choice = input("Enter your choice (A/B/C/D): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform the chosen operation
if choice == 'A':
    print("Result:", num1 + num2)
elif choice == 'B':
    print("Result:", num1 - num2)
elif choice == 'C':
    print("Result:", num1 * num2)
elif choice == 'D':
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Cannot divide by zero!")
else:
    print("Invalid input")
