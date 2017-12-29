import json

filename = 'files/username.json'

print("What would you like to do?")
while True:
    print("Choices:" + "\n 1 - Enter names" + "\n 2 - Read names" + "\n 3 - Quit")
    menu_choice = input("Choice: ")
    if menu_choice == '1':
        username = input("What is your username? ")
        with open(filename, 'a') as f_obj:
            json.dump(username, f_obj)
            print("Your name has been added, " + username + ".")
    elif menu_choice == '2':
        with open(filename) as f_obj:
            usernames = json.load(f_obj)
        print(usernames)
    elif menu_choice == '3':
        break
    else:
        print("That is not a valid choice. Pick again.")

print("Thank you!")




