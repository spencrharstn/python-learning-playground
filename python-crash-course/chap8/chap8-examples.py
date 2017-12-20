"""Functions"""

def greet_user(username):
    """Display a greeting"""
    print("Hello, " + username.title() + "!")

greet_user('bob') #passing an argument

def describe_pet(animal, name):
    """Display a pet's info"""
    print("I have a " + animal + ".")
    print("My " + animal + "'s name is " + name.title() + ".")

describe_pet(name='bob', animal='chinchilla') #using keyword arguments

def describe_pet_alt(name,animal='dog'):
    """Display a pet's info using default values"""
    print("I have a " + animal + ".")
    print("My " + animal + "'s name is " + name.title() + ".")

describe_pet_alt('charlie') #function has a default value
describe_pet_alt('charlie', 'cat') #function has a default value but we change the default value

def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a neatly formatted name, first_name, last_name required; middle_name optional"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

manager = get_formatted_name('michael','scott', 'gary')
asst_manager = get_formatted_name('jim', 'halpert')
print(manager)
print(asst_manager)

def build_person(first_name, last_name, age=''):
    """Return a dictionary of information about a person; age optional"""
    person = {'first':first_name, 'last':last_name}
    if age:
        person['age'] = age
    return person

receptionist = build_person('pam','beesley', 32)
temp_person = build_person('ryan','howard')
print(receptionist)
print(temp_person)

# def make_pizza(size, *toppings):
#     """Print list of toppings that have been requested, using an arbitrary number of toppings"""
#     print("The " + str(size) + "-inch pizza needs:")
#     for topping in toppings:
#         print(" - " + topping)

# make_pizza(16,'pepperoni')
# make_pizza(20,'ham', 'pineapple','bacon')

def build_user(first, last, **user_info):
    """Build a dictionary containing user info"""
    profile = {}
    profile['first'] = first
    profile['last'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_user('dwight', 'schrute', location='schrute farms', occupation='salesman')
print(user_profile)

#Using a module that stores a function
from pizza import make_pizza as mp
mp(16, 'pepperoni')
mp(20, 'ham', 'pineapple', 'bacon')