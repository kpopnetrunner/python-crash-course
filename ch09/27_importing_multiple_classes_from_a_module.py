# 27_importing_multiple_classes_from_a_module.py

# You can import as many classes as you need into a program file. If we want to
# make a regular car and an electric car in the same file, we need to import
# both classes, Car and ElectricCar:

# my_cars.py

# from car import Car, ElectricCar

# my_beetle = Car('volkswagen', 'beetle', 2019)
# print(my_beetle.get_descriptive_name())

# my_tesla = ElectricCar('tesla', 'roadster', 2019)
# print(my_tesla.get_descriptive_name())

# You import multiple classes from a module by seperating each class with a
# comma 1. Once you've imported the necessary classes, you're free to make as
# many instances of each class as you need.

# In this example, we make a regular Volkswage Beetle at 2 and an electric Tesla
# Roadster at 3:

# 2019 Volkswagen Beetle
# 2019 Tesla Roadster
print("This program contains notes in the comments.")
