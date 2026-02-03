# 02_passing_info_to_a_function.py

# Passing Information to a Function

# Modified slightly, the function greet_user() can not only tell the user Hello!
# but also greet them by name. For the function to do this, you enter username
# in the parentheses of the function's definition at def greet_user(). By adding
# username here you allow the function to accept any value of username you
# specify. The function now expects you to provide a value for username each
# time you call it. When you call greet_user(), you can pass a name, such as
# 'jesse', inside the parentheses:

# def greet_user(username):
#     """Display a simple greeting."""
#     print(f"Hello, {username.title()}!")
# greet_user('jesse')

# Entering greet_user('jesse') calls greet_user() and gives the function the
# information it needs to execute the print() call. The function accepts the
# name you passed it and displays the greeting for that name:

# Hello, Jesse!

# Likewise, entering greet_user('sarah') calls greet_user(), passes it 'sarah',
# and prints Hello, Sarah! You can call greet_user() as often as you want and
# pass it any name you want to produce a predictable output every time.
print("This program contains notes in the comments.")
