from name_function import get_formatted_name

print("Enter 'q' at anytime to quit.")
while True:
    first = input("\nEnter a first name: ")
    if first == 'q':
        break
    last = input("Enter a last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print("\tNeatly formatted name: " + formatted_name + ".")