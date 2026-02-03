# 10_default_values.py

# Default Values

# When writing a function, you can define a default value for each parameter.
# If an argument for a parameter is provided in the function call, Python uses
# the argument value. If not, it uses the parameter's default value. So when
# you define a default value for a parameter, you can exclude the corresponding
# argument you'd usually write in the function call. Using default values can
# simplify your function calls and clarify the ways in which your functions are
# typically used.

# For example, if you notice ethat most of the calls to describe_pet() are being
# used to describe dogs, you can set the default value of animal_type to 'dog'.
# Now anyone calling describe_pet() for a dog can omit that information:

# def describe_pet(pet_name, animal_type='dog'):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet(pet_name='willie')

# We've changed the definiton of describe_pet() to include a default value,
# 'dog', for animal_type. Now when the function is called with no animal_type
# specified, Python knows to use the value 'dog' for this parameter:

# I have a dog.
# My dog's name is Willie.

# Note that the order of parameters in the function definition had to be
# changed. Because the default value makes it unnecessary to specify a type of
# animal as an argument, the only argument left in the function call is the
# pet's name. Python still interprets this as a positional argument, so if the
# function is called with just a pet's name, that argument will match up with
# the first parameter listed in the function's definition. This is the reason
# the first parameter needs to be pet_name.

# The simplest way to use this function is to provide just a dog's name in the
# function call:

# describe_pet('willie')

# This function call would have the same output as the previous example. The
# only argument provided is 'willie', so it is matched up with the first
# parameter in the definition, pet_name. Because no argument is provided for
# animal_type, Python uses the default value 'dog'.

# To describe an animal other than a dog, you could use a function call like
# this:

# describe_pet(pet_name='harry', animal_type='hamster')

# Because an explicit argument for animal_type is provided, Python will ignore
# the parameter's default value.

# NOTE

# When you use default values, any parameter with a default value needs to be
# listed after all the parameters that don't have default values. This allows
# Python to continue interpreting positional arguments correctly.
print("This program contains notes in the comments.")
