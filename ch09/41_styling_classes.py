# 41_styling_classes.py

# Styling Classes

# A few styling issues related to classes are worth clarifying, especially as
# your programs become more complicated.

# Class names should be written in CamelCase. To do this, Capitalize the first
# letter or each word in the name, and don't use underscores. Instance and
# module names should be written in lowercase with underscores between words.

# Every class should have a docstring immediately following the class definition
# . The docstring should be a brief description of what the class does, and you
# should follow the same formatting conventions you used for writing docstrings
# in functions. Each module should also have a docstring describing what the
# classes in a module can be used for.

# You can use blank lines to organize code, but don't use them excessively.
# Within a class you can use one blank line between methods, and within a module
# you can use two blank lines to separate classes.

# If you need to import a module from the standard library and a module that you
# wrote, place the import statement for the standard library module first. Then
# add a blank line and the import statement for the module you wrote. In
# programs with multiple import statements, this convention makes it easier to
# see where the different modules used in the program come from.

# Summary

# In this chapter you learned how to write your own classes. You learned how to
# store information in a class using attributese and how to write methods that
# give your classes the behavior they need. You learned to write __ini__()
# methods that create instances from your classes with exactly the attributes
# you want. You saw how to modify the attributes of an instance directly and
# through methods. You learned that inheritance can simplify the creation of
# classes that are related to each other, and you learned to use instances of
# one class as attributes in another class to keep each class simple.

# You saw how storing classes in modules and importing classes you need into the
# files where they'll be used can keep your projects organized. YOu started
# learning about the Python standard library, and you saw an example based on
# the random module. Finally, you learned to style your classes using Python
# conventions.

# In Chapter 10 you'll learn to work with files so you can save the work you've
# done in a program and the work you've allowed users to do. You'll also learn
# about exceptions, a special Python class designed to help you respond to
# errors when they arise.
print("This program contains notes in the comments.")
