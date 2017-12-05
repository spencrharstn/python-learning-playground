#!/usr/bin/env python

""" Takes a string to see if it is a valid palindrome """

import re

def reverse(input_string):
    """Reverses a string and returns it"""

    reverse_string = []

    for letter in range(len(input_string) - 1, 0-1, -1):
        reverse_string.append(input_string[letter])

    result = "".join(reverse_string)
    return result

def palindrome(input_string):
    """Returns True/False if a string is a palindrome"""

    # Remove any non-alpha characters from string and make it all lowercase
    input_string = re.sub(r'[^a-zA-Z]', '', input_string.lower())

    # Get the reversed string
    reverse_string = reverse(input_string)

    for i, letter in enumerate(input_string):
        if letter != reverse_string[i]:
            return False
    return True

def main():
    """The main function"""

    user_string = input("Enter a string: ")

    # Alternatively, read a palindrome from a text file
    # file = open('palindrome.txt', 'r')
    # user_string = file.read()
    # file.close()

    print("\nString:\n\t", user_string)
    print("\nReversed:\n\t", reverse(user_string))
    if palindrome(user_string):
        print('The string is a palindrome!')
    else:
        print('The string is not a palindrome!')

if __name__ == '__main__':
    main()
