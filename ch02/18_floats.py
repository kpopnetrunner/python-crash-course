# Floats

# Python calls any number with a decimal point a float. This term is used in most programming
# languages, and it refers to the fact that a decimal point can appear at any position in a
# number. Every programming language must be carefully designed to properly manage decimal
# numbers so numbers behave appropriately no matter where the decimal point appears.

# For the most part, you can use decimals without worrying about how they behave. Simply enter
# the numbers you want to use, and Python will most likely do what you expect:
# >>> 0.1 + 0.1
# 0.2
# >>> 0.2 + 0.2
# 0.4
# >>> 2 * 0.1
# 0.2
# >>> 2 * 0.2
# 0.4

# But be aware that you can sometimes get an artitrary number of decimal places in your answer:
# >>> 0.2 + 0.1
# 0.30000000000000000004
# >>> 3 * 0.1
# 0.30000000000000000004

# This happens in all languages and is of little concern. Python tries to find a way to represent
# the result as precisely as possible, which is sometimes difficult given how computers have to
# represent numbers internally. Just ignore the extra decimal places for now; you'll learn ways to
# deal with the extra places when you need to in the projects in Part II.
print("This program contains notes in the comments.")
