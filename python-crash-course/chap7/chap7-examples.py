"""User input and while loops"""

message = input("Tell me something and I'll repeat it: ")
print(message)

name = input("Please enter your name: ")
print("Hello, " + name + "!")

prompt = "Tell us who you are"
prompt += "\nWhat is your first name? "

name = input(prompt)
print("\nHello, " + name + ".")

age = int(input("How old are you? "))

print("You are " + str(age) + " years old")

# while loops
current_number = 1
while current_number <= 10:
    print(current_number)
    current_number += 1

prompt = "\nGive me a number and I'll tell you if it's even or odd:"
prompt += "\n Enter 'q' to quit: "
number = ""
# while number != 'q':
#     number = input(prompt)
#     if number != 'q':
#         number = int(number)
#         if number % 2 == 0:
#             print("\n\tThe number " + str(number) + " is even.")
#         else:
#             print("\n\tThe number " + str(number) + " is odd.")

#using a flag
active = True
while active:
    number = input(prompt)
    if number == 'q':
        active = False
    else:
        number = int(number)
        if number % 2 == 0:
            print("\n\tThe number " + str(number) + " is even.")
        else:
            print("\n\tThe number " + str(number) + " is odd.")

#using break
prompt = "Enter a city (enter 'q' to quit): "
while True:
    city = input(prompt)
    if city == 'q':
        break
    else:
        print("I'd like to go to " + city.title() + ".")



