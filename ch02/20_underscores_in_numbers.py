# Underscores in Numbers

# When you're writing long numbers, you can group digits using underscores to make large numbers more
# readable:

# >>> universe_age = 14_000_000_000

# When you print a number that was defined using underscores, Python prints only the digits:
# >>> print(universe_age)
# 14000000000

# Python ignores the underscores when storing these kinds of values. Even if you don't group the digits
# in threes, the value will still be unaffected. To Python, 1000 is the same as 1_000, which is the same
# as 10_00. This feature works for integers and floats, but it's only available in Python 3.6 and later.
print("This program contains notes in the comments.")
