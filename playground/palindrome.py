# Palindrome
# Takes a string to see if it is a valid palindrome

import re

def reverse(input_string):
	reverse = []

	for letter in range(len(input_string) - 1, 0-1, -1):
		reverse.append(input_string[letter])

	result = "".join(reverse)
	return result

def palindrome(input_string):
	# Remove any non-alpha characters from string and make it all lowercase
	input_string = re.sub(r'[^a-zA-Z]', '', input_string.lower())

	# Get the reversed string
	reverse_string = reverse(input_string)

	for letter in range(len(input_string)):
		#print("\tinput: ", input_string[letter], "\treverse: ", reverse_string[letter])
		if (input_string[letter] != reverse_string[letter]):
			return False
	return True

string = input("Enter a string: ")

# Read a palindrome from a text file
# file = open('palindrome.txt', 'r')
# string = file.read()
# file.close()

print("\nString:\n\t", string)
print("\nReversed:\n\t", reverse(string))

if (palindrome(string)):
	print('The string is a palindrome!')
else:
	print('The string is not a palindrome!')
