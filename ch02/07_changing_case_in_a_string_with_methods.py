# One of the simplest taks you can do wit hstrings is change the nase of the words in a string. Look at the
# following code, and try to determine what's happening:

# In this example, the variable name refers to the lowercase string "ada lovelace". The method title() appears
# after the variable in the print() call. A method is an action that Python can perform on a piece of data.
# The dot (.) after name in name.title() tells Python to make the title() method act on the variable name.
# Every method is followed by a set of parentheses, because methods often need additional information to do their
# work. That information is provided inside the parenteses. The title() function doesn't need any additional
# information, so its parentheses are empty.

# The title() method changes each word to title case, where each word begins with a capital letter. This is useful
# because you'll often want to think of a name as a piece of information. For example, you might want your program
# to recognize the input values Ada, ADA, and ada as the same name, and display all of them as Ada.

# Several other useful methods are available for dealing with case as well. For example, you can change a string 
# to all uppercase or all lowercase letters like this:

# name = "Ada Lovelace"
# print(name.upper())
# print(name.lower())

# This will display the following:

# ADA LOVELACE
# ada lovelace

# The lower() method is particularly useful for storing data. Many times you won't want to trust the
# capitalization that your users provide, so you'll convert strings to lowercase before storing them. Then when
# you want to display the information, you'll use the case that makes the most sense for each string.

name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())
