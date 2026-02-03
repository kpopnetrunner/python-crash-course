# 07_multiple_function_calls.py

# Multiple Function Calls

# You can call a function as many times as need. Describing a second, different
# pet requires just one more call to describe_pet():

# def_describe_pet(animal_type, pet_name):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet('hamster', 'harry')
# describe_pet('dog', 'willie')

# In this second function call, we pass describe_pet() the arguments 'dog' and
# 'willie'. As wit hthe previous set of arguments we used, Python matches 'dog'
# wit the parameter animal_type and 'willie' with the parameter pet_name.

# As before, the function does its job, but this time it prints values for a dog
# named Willie. Now we have a hamster named Harry and a dog named Willie.

# I have a hamster.
# My hamster's name is Harry.

# I have a dog.
# My dog's name is Willie.

# Calling a function multiple times is a very efficient way to work. The code
# describing a pet is written once in the function. Then, anytime you want to
# describe a new pet, you call the function wit hthe new pet's information. Even
# if the code for describing a pet were to expand to ten lines, you could still
# describe a new pet in just one line by calling the function again.

# You can use as many positional arguments as you need in your functions. Python
# works through the argumetns you provide when calling the function and matches
# each one with the corresponding parameters in the function's definition.

print("This program contains notes in the comments.")
