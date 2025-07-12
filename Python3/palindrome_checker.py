# This program checks if the entered word is a palindrome

# Ask user for input
word = input("Enter a word: ")

# Reverse the word using slicing
reversed_word = word[::-1]

# Check if it's the same forward and backward
if word == reversed_word:
    print(word, "is a palindrome.")
else:
    print(word, "is not a palindrome.")
