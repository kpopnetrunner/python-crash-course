# 19_using_a_function_with_a_while_loop.py

# You can use functions with all the Python structures you've learned about so
# far. For example, leet's use the get_formatted_name() function with a while
# loop to greet users more formally. Here's a first attempt at greeting people
# using their first and last names:

# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = f"{first_name}, {last_name}"
#     return full_name.title()

#   This is an infinite loop!
#   While True:
# 1     print("\nPlease tell me your name:")
#       f_name = input("First name: ")
#       l_name = input("Last name: ")

#       formatted_name = get_formatted_name(f_name, l_name)
#       print(f"\nHello, {formatted_name}!")

# For this example, we use a simple version of get_formatted_name() that doesn't
# involve middle names. The while loop asks the user to enter their name, and we
# prompt for their first and last name separately 1. But there's one problem
# with this whileLoop: We haven't defined a quit condition. Whre do you put a
# quit condition when you ask for a series of inputs? We want the user to be
# able to quit as easily as possible, so each prompt should offer a way to quit.
# The break statement offers a straightforward way to exit the loop at either
# prompt:

# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = f"{first_name}, {last_name}"
#     return full_name.title()

# This is an infinite loop!
# while True:
#     print("\nPlease tell me your name:")
#     print("(enter 'q' at any time to quit)")

#     f_name = input("First name: ")
#     if f_name == 'q':
#         break

#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break

#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello, {formatted_name}!")

# We add a message ethat informas the user how to quit, and then we break out of
# the loop if the user enters the quit value at either prompt. Now the program
# will continue greeting people until someone enters 'q' for either name:

# Please tell me your name:
# (enter 'q' at any time to quit)
# First name: eric
# Last name: matthes

# Hello, Eric Matthes!

# Please tell me your name:
# (enter 'q' at any time to quit)
# First name: q
print("This program contains notes in the comments.")
