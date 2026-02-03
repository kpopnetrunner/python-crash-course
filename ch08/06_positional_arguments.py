# 06_positional_arguments.py

# Passing Arguments

# Because a function definition can have multiple paramenters, a function call
# may need multiple arguments. You can pass arguments to your functions in a
# number of ways. You can use positional arguments, which need to be in the same
# order the parameters were written: keyword arguments, where each argument
# consists of a variable name and a value; and lists and dictionaries of values.
# Let's look at each of these in turn.

# Positional Arguments

# When you call a function, Python must match each argument in the function
# call with a parameter in the function definition. The simplest way to do this
# is based on the order of the arguments provided. Values matched up this way
# are called positional arguments.

# To see how this works, consider a function that displays information about
# pets. The function tells us what kind of animal each pet is and the pet's name
# , as shown here:

# def_describe_pet(animal_type, pet_name):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet('hamster', 'harry')

# The defintion shows that this function eeds a type of animal and the animal's
# name 1. When we call describe_pet(), we need to provide an animal type and a
# name, in that order. For example, in the function call, the argument 'hamster'
# is assigned to the parameter animal_type and the argument 'harry' is assigned
# to the parameter pet_name 2. In the function body, these two parameters are
# used to display information about the pet being described.

# The output describes a hamster named Harry:

# I have a hamster.
# My hamster's name is Harry.

print("This program contains notes in the comments.")
