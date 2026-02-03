# 03_accessing_attributes.py

# 1 class Dog:
# 2     """A simple attempt to model a dog."""
#
# 3     def __init__(self, name, age):
#           """Initialize name and age attributes."""
# 4         self.name = name
#           self.age = age
#
# 5     def sit(self):
#           """Simulate a dog sitting in response to a command."""
#           print(f"{self.name} is now sitting.")
#
#       def roll_over(self):
#           """Simulate rolling over in response to a command."""
#           print(f"{self.name} rolled over!")

# 1 my_dog = Dog('Willie', 6)

# 2 print(f"My dog's name is {my_dog.name}.")
# 3 print(f"My dog is {my_dog.age} years old.")

# To access the attributes of an instance, you use dot notation. At 2 we access
# the value of my_dog's attrubute name by writing:

# my_dog.name

# Dot notation is used often in Python. This syntax demonstrates how Python
# find an attribute's value. Here Python looks at the instance my_dog and then
# finds the attribute name associated with my_dog. This is the same attribute
# referrred to as self.name in the class Dog. At 3 we use the same approach to
# work with the attribute age.

# The output is a summary of what we know about my_dog:

# My dog's name is Willie.
# My dog is 6 years old.
print("This program contains notes in the comments.")
