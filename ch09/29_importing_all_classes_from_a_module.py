# 29_importing_all_classes_from_a_module.py

# You can import every class from a module using the following syntax:

# from module_name import *

# This module name is not recommended for two reasons. First, it's helpful to be
# able to read the import statements at the top of a file and get a clear sense
# of which clases a program uses. With this approach it's unclear which classes
# you're using from the module. This approach can also lead to confusion with
# names in the file. If you accidently import a class with the same name as
# something else in your program file, you can create errors that are bard to
# diagnose. I show this here because even though it's not a recommended approach
# , you'll likely see it in other people's code at some point.

# If you need to import many classes from a module, you're better off importing
# the entire module and using the module_name.ClassName syntax. You won't see
# all the classes used at the top of the file, but you'll see clearly where the
# module is used in the program. You'll also avoid the potential naming
# conflicts that can arise when you import every class in a module.
print("This program contains notes in the comments.")
