# 02_making_an_instance_from_a_class.py

# Think of a class as a set of instructions for how to make an instance. The
# class Dog is a set of instructions that tells Python how to make individual
# instances representing specific dogs.

# Let's name an instance representing a specific dog:

class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

# The Dog class we're using here is the one we just wrote in the previous
# example. At 1 we well Python to create a dog whose name is 'Willie' and whose
# age is 6. When Python reads this line, it calls the __init__() method in Dog
# with the arguments 'Willie' and 6. The __init__() method creates an instance
# representing this particular dog and sets the name and age attributes using
# the values we provided. Python then returns an instance representing this dog.
# We assign that instance to the variable my_dog. The naming convention is
# helpful here: we can usually assume that a capitalized name like Dog refers
# to a class, and a lowercase name like my_dog refers to a single instance
# created from a class.
