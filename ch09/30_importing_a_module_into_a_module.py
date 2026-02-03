# 30_importing_a_module_into_a_module.py

# Sometimes you'll want to spread out your classes over several modules to keep
# any one file from growing too large and avoid storing unrelated classes in the
# same module. When you store your classes in several modules, you may find that
# a class in one module depends on a class in another module. When this happens,
# you can import the required class into the first module.

# For example, let's store the Car class in one module and the ElectricCar and
# Battery classes in a separate module. We'll make a new module called
# electric_car.py--replacing the electric_car.py file we created earlier--and
# copy just the Battery and ElectricCar classes into this file:

# electric_car.py
# """A set of classes that can be used to represent electric cars."""

# from car import Car                                                         #1

# class Battery:
#     --snip--

# class ElectricCar(Car):
#     --snip--

# The class ElectricCar needs access to its parent class Car, so we import Car
# directly into the module at 1. If we forget this line, Python will raise an
# error when we try to import the electric_car module. We also need to update
# the Car module so it contains only the Car class:

# car.py
# """A clas that can be used to represent a car."""

# class Car:
#     --snip--

# Now we can import each module seperately and create whatever kind of car we
# need:

# my_cars.py

# from car import Car                                                         #1
# from electric_car import ElectricCar

# my_beetle = Car('volkswagen', 'beetle', 2019)
# print(my_beetle.get_descriptive_name())

# my_tesla = ElectricCar('tesla', 'roadster', 2019)
# print(my_tesla.get_descriptive_name())

# At 1 we import Car from its module, and ElectricCar from its module. We then
# create one regular car and one electric car. Both kinds of cars are created
# correctly:

# 2019 Volkswagen Beetle
# 2019 Tesla Roadster
print("This program contains notes in the comments.")
