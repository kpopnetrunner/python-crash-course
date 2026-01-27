# Save each of the following exercises as a separate file with a name like name_cases.py. If you get stuck,
# take a break or see the suggestions in Appendix C.

# 2-7. Stripping Names. Use a variable to represent a person's name, and include some whitespace characters
# at the beginning and end of the name. Make sure you use each character combination, "\t" and "\n", at least
# once.

# Print the name once, so the whitespace around the name is displayed. Then print the name using each of the
# three stripping functions, lstrip(), rstrip(), and strip().

name = "\tyeji hwang\n"
print('The variable "name" is assigned as, "\\tyeji hwang\\n."')
print("Using the print() method:")
print(name)
print("Using the lstrip() method:")
print(name.lstrip())
print("Using the rstrip() method:")
print(name.rstrip())
print("Using the strip() method:")
print(name.strip())
