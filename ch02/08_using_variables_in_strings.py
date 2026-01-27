# Using Variables in Strings

# In some situations, you'll want to use a variable's value inside a string. For example, you might
# want two variables to represent a first name and a last name respectively, and then want to combine
# those values to display someone's full name:

# To insert a variable's value into a string, place the letter f immediately before the opening
# quotation mark. Put braces around the name or names of any variable you want to use inside the string.
# Python will replace each variable with its value when the string is displayed.

# These values are called f-strings. The f is for format, because Python formats the string by replacing
# the name of any variable in braces with its value. The output from the previous code was "ada lovelace."

# You can do a lot with f-strings. For example, you can use f-strings to compose complete messages using
# the information associated with a variable, as shown here:

# The full name is used in a stenence that greets the user, and the title() method changes the name to
# titlecase. This code returns a simple, but nicely formatted greeting:

# Hello, Ada Lovelace!

# You can also use f-strings to compose a message, and then assign the entire message to a variable.

# This code displays the message Hello, Ada Lovelace! as well, but by assigning the message to a variable
# we make the final print() call much simpler.

# NOTE

# F-strings were first introduced in Python 3.6. If you're using Python 3.5 or earlier, you'll need to use
# the format() method rather than this f syntax. To use format(), list the variables you want to use in the
# string inside the parentheses following format. Each variable is referred to by a set of braces; the braces
# will be filled by the values listed in parentheses in the order provided:

# full_name = "{} {}".format(first_name, last_name)

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}!")
message = f"Hello, {full_name.title()}!"
print(message)
