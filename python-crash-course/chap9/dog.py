"""A simple Dog class"""

class Dog():
    """A simple attempt to model a Dog"""
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate a dog rolling over"""
        print(self.name.title() + " rolled over.")
        