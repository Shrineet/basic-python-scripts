# This program counts how many words are in a text file

# Ask the user to enter the filename
filename = input("Enter the filename (with .txt): ")

try:
    # Open the file in read mode
    with open(filename, 'r') as file:
        content = file.read()  # read the entire file as a string
        words = content.split()  # split the string into words
        print("Total number of words:", len(words))
except FileNotFoundError:
    print("File not found. Please check the filename.")
