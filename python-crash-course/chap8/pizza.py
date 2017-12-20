"""Module to create a pizza"""

def make_pizza(size, *toppings):
    """Print list of toppings that have been requested, using an arbitrary number of toppings"""
    print("The " + str(size) + "-inch pizza needs:")
    for topping in toppings:
        print(" - " + topping)