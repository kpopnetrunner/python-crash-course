# 35_importing_an_entire_module.py

# Storing Your Functions in Modules

# One advantage of functions is the way they separate blocks of code from your
# main program. By using descriptive names for your functions, you main
# program will be much easier to follow. You can go a step further by storing
# your functions in a separate file called a module and then importing that
# module into your main program. An import statement tells Python to make the
# code in a module available in the currently running program file.

# Storing your functions in a separate file allows you to hid the details of
# your program's code and focus on it's higher-level logic. It also allows you
# to reuse functions in many different programs. When you store your functions
# in separate files, you can share those files with other programmers without
# also having to share your entire program. Knowing know to import functions
# also allows you to use libraries of functions that other programmers have
# written.

# There are several ways to import a module, and I'll show you each of these
# briefly.

# Importing an Entire Module

# To start importing functions, we first need to create a module. A module is a
# file ending in .py that contains code you want to import into your program.
# Let's make a module that contains the function make_pizza(). To make this
# module, we'll remove everything from the file pizza.py except the function
# make_pizza():

# pizza.py

# def make_pizza(size, *toppings):
#     """Summarize the pizza we are about to make."""
#     print(f"\nMaking a {size}-inch pizza with the following toppings:")
#     for topping in toppings:
#         print(f"- {topping}")

# Now we'll make a separate file called making_pizzas.py in the same directory
# as pizza.py. This file imports the module we just created and then makes
# two calls to make_pizza():

# making_pizzas.py

# import pizza

# pizza.make_pizza(16, 'pepperoni')
# pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# When Python reads this file, the line import pizza tells Python to open the
# file pizza.py and copy all the functions from it into this program. You don't
# actually see code being copied between files because Python copies the code
# behind the scenes just before the program runs. All you need to know is that
# any function defined in pizza.py will now be available in making_pizzas.py.

# To call a function from an imported module, enter the name of the module you
# imported, pizza, followed by the name of the function make_pizza(), separated
# by a dot 1. This code produces the same output as the original program that
# didn't import a module:

# Making a 16-inch pizza with the following toppings:
# - pepperoni

# Making a 12-inch pizza with the following toppings:
# - mushrooms
# - green peppers
# - extra cheese

# The first approach to importing, in which you simply write import followed
# by the name of the module, makes every function from the module available in
# your program. If you use this kind of import statement to import an entire
# module named module_name.py, each function in the module is available through
# the following syntax:

# module_name.function_name()
print("This program contains notes in the comments.")
