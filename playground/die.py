from random import randint

class Die():
    """A class for a simple die"""

    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_die(self):
        """A roll of the die"""
        roll = randint(1, self.sides)
        return roll