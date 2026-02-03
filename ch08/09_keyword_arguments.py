# 09_keyword_arguments.py

# Keyword Arguments

# A keyword argument is a name-value pair that you pass to a function. You
# directly associate the name and the value within the argument, so when you
# pass the argument to the function, there's no confusion (you won't end up
# with a harry named Hamster). Keyword arguments free you from having to
# worry about correctly ordering your aruments in the function call, and they
# clarify the role of each value in the function call.

# Let's rewrite pets.py using keyword arguments to call describe_pets():

# def describe_pet(naimal_type, pet_name):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet(animal_type='hamster', pet_name='harry')

# The function describe_pet() hasn't changed. But when we call the function,
# we explicitly tell Python which parameter each argument should be matched
# with. When Python reads the function call, it knows to assign the argument
# 'hamster' with the parameter animal_type and the argument 'harry' to pet_name.
# The output correctly shows that we have a hamster named Harry.

# The order of keyword arguments doesn't matter because Python knows where each
# value should go. The following two function calls are equivalent:

# describe_pet(animal_type='hamster', pet_name='harry')
# describe_pet(pet_name='harry', animal_type='hamster')

# NOTE
# When you use keyword arguments, be sure to use the exact name of the
# parameters in the function's definition.
print("This program contains notes in the comments.")
