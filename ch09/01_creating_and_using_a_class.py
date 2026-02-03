# 01_creating_and_using_a_class.py

# Object-oriented programming is one of the most effective approaches to writing
# software. In object-oriented programming you write classes tht represent
# real-world things and situations, and you create objects based on these
# classes. When you write a class, you define the general behavior that a whole
# category of objects can have.

# When you create individual objects from the class, each object is
# automatically equipped with the general behavior; you can then give each
# object whatever unique traits you desire. You'll be amazed how real-world
# situations can be modeled with object-oriented programming.

# Making an object from a class is called instatiation, and you work with
# instances of a class. In this chapter you'll write classes and create instances
# of those classes. You'll specify the kind of information that can be stored in
# instances, and you'll define actions that can be taken with these instances.
# You'll also write classes that extend the functionality of existing classes,
# so similar classes can share code efficiently. You'll store your classses in
# modules and import classes written by other programmers into your own program
# files.

# Understanding object-oriented programming will help you see the world as a
# programmer does. It'll help you really know your code, not just what's
# happening line by line, but also the bigger concepts behind it. Knowing the
# logic behind classes will train you to think logically so you can write
# programs that effectively address almost any problem you encounter.

# Classes also make life easier for you and other programmers you'll work with
# as you take on increasingly complex challenges. When you and other programmers
# write code based on the same kind of logic, you'll be able to understand each
# other's work. Your programs will make sense to many collaborators, allowing
# everyone to accomplish more.

# Creating and Using a Class

# You can model almost anything using classes. Let's start by writing a simple
# class, Dog, that represents a dog--not one dog in particular, but any dog.
# What do we know about most pet dogs? Well, they have a name and age. We also
# know that most dogs sit and roll over. Those two pieces of information
# (name and age) and those two behaviors (sit and roll over) will go in our Dog
# class because they're common to most dogs. This class will tell Python how to
# make an object representing a dog. After our class is written, we'll use it to
# make individual instances, each of which represents one specific dog.

# Creating the Dog Class

# Each instance created from the dog class will store a name and an age, and
# we'll give each dog the ability to sit() and roll_over():

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

# There's a lot to notice here, but don't worry. You'll see this structure
# throughout this chapter and have lots of time to get used to it. At 1 we
# define a class called Dog. By convention, capitalized names refer to classes
# in Python. There are no parentheses in the class definition because we're
# creating this class from scratch. At 2 we write a docstring describing what
# this class does.

# The __init__() Method

# A function that's part of a class is a method. Everything you learned about
# functions applies to methods as well: the only practical difference for now is
# the way we'll call methods. The __init__() method at 3 is a special method
# that Python runs automatically whenever we create a new instance based on the
# Dog class. This method has two leading underscores and two trailing
# underscores, a convention that helps prevent Python's default method names
# from conflicting with your method names. Make sure to use two underscores on
# each side of __init__(). If you use just one on each side, the method won't be
# called automatically when you use your class, which can result in errors that
# are difficult to identify.

# We define the __init__() method to have three parameters: self, name, and age.
# The self parameter is required in the method defintion, and it must come first
# before the other parameters. It just be included in the definition because
# when Python calls this method later (to create an instance of Dog), the method
# call will automatically pass the self argument. Every method call associated
# with an instance automatically passes self, which is a reference to the
# instance itself; it gives the individual instance access to the attributes and
# methods in the class. When we make an instance of Dog, Python will call the
# __init__() method from the Dog class. We'll pass Dog() a name and an age as
# arguments; self is passed automatically, so we don't need to pass it. Whenever
# we want to make an instance from the Dog class, we'll provide values for only
# the last two parameters, name and age.

# The two variables defined at 4 each have the prefix self. Any variable
# prefixed with self is available to every method in the class, and we'll also
# be able to access these variables through any instancecreated from the class.
# The line self.name = name takes the value associated with the parameter name
# and assigns it to the variable name, which is then attached to the instance
# being created. The same process happens with self.age = age. Variables that
# are accessible through instances like this are called attributes.

# The Dog class has two other methods defined: sit() and roll_over() 5. Because
# these methods don't need additional information to run, we just define them
# to have one parameter, self. The instances we create later will have access
# to these methods. In other words, they'll be able to sit and roll over.
# For now, sit() and roll_over() don't do much. They simply print a message
# saying the dog is sitting or rolling over. But the concet can be extended to
# realistic situations: if this class were part of an actual computer game,
# these methods would contain code to make an animated dog sit and roll over. If
# this class was written to control a robot, these methods would direct
# movements that cause a robotic dog to sit and roll over.

print("This program contains notes in the comments.")
