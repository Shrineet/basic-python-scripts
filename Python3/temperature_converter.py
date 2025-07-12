# This program converts temperature from Celsius to Fahrenheit or vice versa

print("Temperature Converter")
print("A. Celsius to Fahrenheit")
print("B. Fahrenheit to Celsius")

choice = input("Enter A or B: ")

if choice == 'A':
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print("Temperature in Fahrenheit:", fahrenheit)
elif choice == 'B':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print("Temperature in Celsius:", celsius)
else:
    print("Invalid choice. Please enter 1 or 2.")
