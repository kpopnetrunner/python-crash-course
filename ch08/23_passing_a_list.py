# 23_passing_a_list.py

# Passing a List

# You'll often find it useful to pass a list to a function, whether it's a list
# of names, numbers or more complex objects, such as dictionaries. When you pass
# a list to a function, the function gets direct access to the contents of the
# list. Let's use functions to make morking ith lists more efficient.

# Say we have a list of users and want to print a greeting to each. The
# following example sends a list of names to a function called greet_users(),
# which greets each person in the list individually:

# def greet_users(names)
#     """Print a simple greeting to each user in the list."""
#     for name in names:
#         msg = f"Hello, {name.title()}!"
#         print(msg)

# usernames = ['hannah', 'ty', 'margot']
# greet_users(usernames)

# We define greet_users() so it expects a list of names, which it assigns to
# the parameter names. The function loops through the list it receives and
# prints a greeting to each user. At 1 we define a list of users and then pass
# the list usernames to greet_users() in our function call:

# Hello, Hannah!
# Hello, Ty!
# Hello, Margot!

# This is the output we wanted. Every user sees a personalized greeting, and you
# can call the function any time you want to greet a specific set of users.
print("This program contains notes in the comments.")
