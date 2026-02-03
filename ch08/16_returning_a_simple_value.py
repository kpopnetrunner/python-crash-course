# 16_returning_a_simple_value.py

# Return Values

# A function doesn't always have to display its output directly. Instead, it can
# process some data and then return a value or a set of values. The value the
# function returns is called a return value. The return statement takes a value
# from inside a function and sends it back to the line that called the function.
# Return values allow you to move much of your program's grunt work into
# functions, which can simplify the body of your program.

# Returning a Simple Value

# Let's look at a function that takes a first and last name, and returns a
# neatly formatted full name:

# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()

# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)

# The definition of get_formatted_name() takes as parameters a first and a last
# name 1. The function combines these two names, adds a space between them, and
# assigns the result to full_name 2. The value of full_name is converted to
# title case, and then returned to the calling line at 3.

# When you call a function that returns a value, you need to provide a variable
# that the return value can be assigned to. In this case, the returned value is
# assigned to the variable musician at 4. The output shows a neatly formatted
# name made up of the parts of a person's name:

# Jimi Hendrix

# This might seem like a lot of work to get a neatly formatted name when we
# could have just written:

# print("Jimi Hendrix")

# But when you consider working with a large program that needs to store many
# first and last names separately, functions like get_formatted_name() become
# very useful. You store first and last names separately and then call this
# function whenever you want to display a full name.

print("This program contains notes in the comments.")
