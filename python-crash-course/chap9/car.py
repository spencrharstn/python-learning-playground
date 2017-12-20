class Car():
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def get_name(self):
        """Return a neatly formatted name"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement with the car's mileage"""
        print("This car has " + str(self.odometer) + " miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer of the car"""
        if mileage < self.odometer:
            print("You can't roll back an odometer!")
        else:
            self.odometer = mileage

    def increment_odometer(self, miles):
        """Add miles to the car"""
        self.odometer += miles