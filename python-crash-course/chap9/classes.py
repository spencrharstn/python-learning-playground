"""Classes - the main file"""

from dog import Dog

my_dog = Dog('charlie', 4)
print("My dog's name is " + my_dog.name.title() + ".")
print(my_dog.name.title() + " is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()


from car import Car
my_car = Car('toyota', 'corolla', 2014)
print("My car is a " + my_car.get_name())
my_car.read_odometer()
my_car.odometer = 19200
my_car.read_odometer()
my_car.update_odometer(19283)
my_car.read_odometer()
my_car.increment_odometer(53)
my_car.read_odometer()
my_car.fill_gas_tank()

from electric_car import ElectricCar
my_electric_car = ElectricCar('nissan','leaf',2017)
print(my_electric_car.get_name())
my_electric_car.battery.describe_battery()
my_electric_car.fill_gas_tank()
my_electric_car.battery.get_range()

import car
my_truck = car.Car('toyota','tacoma', 2016)
print(my_truck.get_name())


from user import User 
user1 = User('arthur','schaffer')
print(user1.get_name())