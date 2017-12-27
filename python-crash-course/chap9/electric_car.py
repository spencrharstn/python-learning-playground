"""A set of classes to represent an electric car"""
from car import Car

class ElectricCar(Car):
    """Represent aspects of a car specific to an electric car"""

    def __init__(self, make, model, year,batt_size=70):
        """Initialize attributes of the parent class. Calls init() of Car"""
        super().__init__(make,model,year)
        self.battery = Battery(batt_size)

    def fill_gas_tank(self):
        """Electric cars don't need gas"""
        print("This car doesn't need gas.")

class Battery():
    """A simple battery class"""

    def __init__(self, battery_size):
        """Initialize batery attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Describe the size of the battery"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Print how much range this battery provides"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range) + " miles on a full charge."
        print(message)