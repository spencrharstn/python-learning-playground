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
