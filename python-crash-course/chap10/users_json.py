import json

filename = 'files/username.json'

def input_user():
    """Prompt for new username"""
    username = input("What is your username? ")
    if username:
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
        print("Your name has been added, " + username + ".")
    else:
        print("You must enter a valid username.")

def read_user():
    """Get stored username, if available, and greet the user"""
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        print("The file does not exist.")
    except json.decoder.JSONDecodeError:
        print("No username is stored.")
    else:
        print("Welcome back, " + username)

def main():
    print("What would you like to do?")
    while True:
        print("Menu:" + "\n 1 - Enter username" + "\n 2 - Read username" + "\n 3 - Quit")
        menu_choice = input("Choice: ")
        if menu_choice == '1':
            input_user()
        elif menu_choice == '2':
            read_user()
        elif menu_choice == '3':
            break
        else:
            print("That is not a valid choice. Pick again.")

    print("Thank you!")

main()