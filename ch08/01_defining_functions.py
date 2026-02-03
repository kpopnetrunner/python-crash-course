# 01_defining_functions.py

# In this chapter, you'll learn to write functions, which are named blocks of
# code that are designed to do one specific job. When you want to perform a
# particular task that you've defined in a function, you call the function
# responsible for it. If you need to perform that task multiple times throughout
# your program, you don't need to type all the code for the same task again and
# again; you just call the function dedicated to handling that task, and the
# call tells Python to run the code inside the function. You'll find that using
# functions makes your programs easier to write, read, test, and fix.

# In this chapter you'll also learn ways to pass information to functions.
# You'll learn how to write certain functions whose primary job is to display
# information and other functions designed to process data and return a value
# or a set of values. Finally, you'll learn to store functions in separate files
# called modules to help organize your main program files.

# Defining a Function

# Here's a simple function named greet_user() that prints a greeting:

# 1 def greet_user():
# 2     """Display a simple greeting."""
# 3     print("Hello!")
# 4 greet_user()

# This example shows the simplest structure of a function. The line at 1 uses
# the keyword def to informa Python that you're defining a function. This is the
# function definition, which tells Python the name of the function and, if
# applicable, what kind of information the function needs to do its job. The
# parentheses hold that information. In this case, the name of the function is
# greet_user(), and it needs no information to do its job, so its parentheses
# are empty. (Even so, the parentheses are required.) Finally, the definition
# ends in a colon.

# Any indented lines that follow def greet_user(): make up of the body of the
# function. The text at 2 is a comment called a docstring, which describes what
# the function does. Docstrings are enclosed in triple quotes, which Python
# looks for when it generates documentation for the functions in your programs.

# The line print("Hello!") 3 is the only line of actual code in the body of this
# function, so greet_user() has just one job: print("Hello!").

# When you want to use this function, you call it. A function call tells Python
# to execute the code in the function. To call a function, you write the name of
# the function, followed by any necessary information in parentheses, as shown
# at 4. Because no information is needed here, calling our function is as simple
# as entering greet_user(). As expected, it prints Hello!:

# Hello!
print("This program contains notes in the comments.")
