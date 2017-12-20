"""Dictionaries"""

# Example dictionary
alien_0 = {'color': 'green', 'points': 5, 'speed': 'slow'}

print(alien_0['color'])
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points")

# add new key-value pairs
alien_0['x_pos'] = 5
alien_0['y_pos'] = 25

print(alien_0)

# an empty dictionary
alien_1 = {} 
alien_2 = {}
alien_1['color'] = 'yellow'
alien_1['points'] = 10
alien_1['speed'] = 'medium'
alien_2['color'] = 'red'
alien_2['speed'] = 'fast'
print(alien_1)
print(alien_2)

print("Original pos: " + str(alien_0['x_pos']))
# adjust a value of a key-value pair
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_pos'] = alien_0['x_pos'] + x_increment
print("New x pos is: " + str(alien_0['x_pos']))

# remove a key-value pair
del alien_0['points']
print(alien_0)

# dictionary of similar objects
fav_languages = {
    'jen':'python',
    'sarah':'c++',
    'edward':'ruby',
    'phil':'python'
}

print("Sarah's fav language is " + fav_languages['sarah'].title() + ".")

# 6-1 exercise
person_1 = {'first_name':'robert','last_name':'redford','age':'36','city':'hollywood'}
print(person_1)

# 6-2 exercise
fav_numbers = {
    'robert':43,
    'billy':12,
    'jane': 77
}
print(fav_numbers)

# 6-3 exercise
glossary = {
    'range': 'a generated list of numbers',
    'docstring': 'A string that appears as the lexically first expression in a module, class definition or function/method definition',
    'list': 'a sequence of values. only sequence itself is mutable'
}

# loop through a dictionary
for key, value in glossary.items():
    print("\n"+ key.title() + ":")
    print(value)

for name, language in fav_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

# loop through the keys in a dictionary
friends = ['jen', 'edward']
for name in fav_languages.keys(): # or fav_langues() <-- by default it lists the keys
    print(name.title())
    if name in friends:
        print("Hi " + name.title() + ", I see your favorite language is " + fav_languages[name].title() + ".")

# sorted dictionary
for name in sorted(fav_languages.keys()):
    print(name.title() + ", thanks.")

# loop through values
print("All values: ")
for language in fav_languages.values():
    print("\t" + language.title())
# loop through values that are unique
print("Unique:")
for language in set(fav_languages.values()):
    print("\t" + language.title())

# Nesting dictionaries
aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)

print("Making aliens...")
# empty set for aliens
aliens = []
# make a bunch of aliens
for alien_number in range(25):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# change some aliens
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'

# show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")
print("Total aliens: " + str(len(aliens)))

# lists in a dictionary
# a pizza example
pizza = {
    'crust': 'thick',
    'size': 'large',
    'toppings': ['pepperonis', 'mushrooms', 'jalapenos']
}

print("Your pizza is a " + pizza['size'] + " " + pizza['crust'] + " pizza with the following toppings: ")
for topping in pizza['toppings']:
    print("\t" + topping)


# dictionaries in a dictionary
users = {
    'aeinsten': {
        'first_name': 'albert',
        'last_name': 'einstein',
        'location': 'princeton'
    },
    'mcurie': {
        'first_name': 'marie',
        'last_name': 'curie',
        'location': 'paris'
    }
}

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first_name'] + " " + user_info['last_name']
    location = user_info['location']
    print("\tFull Name: " + full_name.title())
    print("\tLocation: " + location.title())