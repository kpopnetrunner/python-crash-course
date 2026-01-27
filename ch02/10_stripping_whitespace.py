# Stripping Whitespace

# Extra whitespace can be confusing in your programs. To programmers 'python' and 'python ' look pretty
# much the same. But to a program, they are two different strings. Python detects the extra space in
# 'python ' and considers it significant unless you tell it otherwise.

# It's important to think about whitespace, because often you'll want to compare two strings to determine
# whether they are the name. For example, one important instance might involve checking people's usernames
# when they log in to a website. Extra whitespace can be confusing in much simpler situations as well.
# Fortunately, Python makes it easy to eliminate extraneous whitespace from data that people enter.

# Python can look for extra whitespace on the right and left sides of a string. To ensure that no whitespace
# exists at the right end of a string, use the rstrip() method.

# >>> favorite_language = 'python '
# >>> favorite_language
# 'python '
# >>> favorite_language.rstrip()
# 'python'
# >>> favorite_language
# 'python '

# The value associated with favorite_language at 1 contains extra whitespace at the end of the string. When
# you ask Python for this value in a terminal session, you can see the space at the end of the value 2. When
# the rstrip() method acts on the variable favorite_language at 3, this extra space is removed. However, it is
# only removed temporarily. If you ask for the value of favorite_language again, you can see that the string looks
# the same as when it was entered, including the extra whitespace 4.

# To remove the whitespace from the string permanently, you have to associate the stripped value with the variable
# name:

# >>> favorite_language = 'python '
# >>> favorite_language = favorite_language.rstrip()
# favorite_language
# 'python'

# To remove the whitespace from the string, you strip the whitespace from the right side of the string and then
# associate this new value with the original variable, as shown at 1. Changing a variable's value is done often
# in programming. This is how a variable's value can be updated as a program is executed or in response to user input.

# You can also strip whitespace from the left side of a string using the lstrip() method, or from both sides at once
# using strip():

# >>> favorite_language = ' python '
# >>> favorite_language.rstrip()
# ' python'
# >>> favorite_language.lstrip()
# 'python '
# >>> favorite_language.strip()
# 'strip'

# In this example, we start with a value that has whitespace at the beginning and the end 1. We then remove the extra
# space from the right side at 2, from the left side at 3, and from both sides at 4. Experimenting with these 
# stripping functions can help you become familiar with manipulating strings. In the real world, these striping functions
# are used most often to clean up user input before it's stored in a program.

print("This program mostly contains notes in the comments.")
