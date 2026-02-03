# 41_printing_models.py

# 8-15. Printing Models: Put the functions for the example printing_models.py
# in a separate file called printing_functions.py. Write an import statement at
# the top of printing_models.py, and modify the file to use the imported
# functions.

# printing_functions.py

# def print_models(unprinted_designs, completed_models):
#     """
#     Simulate printing each design, until none are left.
#     Move each design to completed_models after printing.
#     """
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f"Printing model: {current_design}")
#         completed_models.append(current_design)

# def show_completed_models(completed_models):
#     """Show all the models that were printed."""
#     print("\nThe following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)

# 41_printing_models.py

# from printing_functions import *

# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)

# If I imported using import printing_functions:

# import printing_functions

# printing_functions.print_models(unprinted_designs, completed_models)
# printing_functions.show_completed_models(completed_models)

print("This program contains notes in the comments.")
