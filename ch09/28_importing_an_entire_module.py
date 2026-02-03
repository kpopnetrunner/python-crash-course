# 28_importing_an_entire_module.py

# Importing an Entire Module

# You can also import an entire module and the access the classes you need using
# dot notation. This approach is simple and results in code that is easy to
# read. Because every call that creates an instance of a class includes the
# module name, you won't have naming conflicts with any names used in the
# current file.

# Here's what it looks like to import the entire car module and then create a
# regular car and an electric car:

# import car                                                                  #1

# my_beetle = car.Car('volkswagen', 'beetle', 2019)                           #2
# print(my_beetle.get_descriptive_name())

# my_tesla = car.ElectricCar('tesla', 'roadster', 2019)                       #3
# print(my_tesla.get_descriptive_name())

# At 1 we import the entire car module. We then access the classes we need
# through the module_name.ClassName syntax. At 2 we again create a Volkswagen
# Beetle, and at 3 we create a Tesla Roadster.
print("This program contains notes in the comments.")
