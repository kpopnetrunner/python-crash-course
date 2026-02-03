# 04_calling_methods.py

# Calling Methods

# After we create an instance from the class Dog, we can use dot notation to
# call any method defined in Dog. Let's make our dog sit and roll over:

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
my_dog.sit()
my_dog.roll_over()

# To call a method, give the name of the instance (in this case, my_dog) and the
# method you want to call, seperated by a dot. When Python reads my_dog.sit(),
# it looks for the method sit() in the class Dog and runs that code. Python
# interprets the line my_dog.roll_over() in the same way.

# Now Willie does what we tell him to:

# Willie is now sitting.
# Willie rolled over!

# This syntax is quite useful. When attributes and methods have been given
# appropriately descriptive names like name, age, sit(), and roll_over(), we can
# easily infer what a block of code, even once we've never seen before, is
# supposed to do.
