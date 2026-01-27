# Every programmer makes mistakes, and most make mistakes every day. Although good programmers might create
# errors, they also know how to respond to those errors efficiently. Let's look at an error you're likely to make early on and learn how to fix it.

# We'll write some code that generates an error on purpose. Enter the following code, including the misspelled
# word mesage shown in bold.

#  When an error occurs in your program, the Python interpreter does its best to help you figure out where the
# problem is. The interpreter provides a traceback when a program cannot run successfully. A traceback is a record
# of where the interpreter ran into trouble when trying to execute your code. Here's an example of a traceback
# that Python provides after you've accidentally misspelled a variable name:

# 0 Traceback (most recent call last):
# 1 File "hello_world.py", line 2, in <module>
# 2     print(mesage)
# 3 NameError: name 'mesage' is not defined

# The output at 1 reports that an error occurs in line 2 of the file hello_world.py. The interpreter shows this
# line 2 to help us spot the error name error and reports that the variable being printed, mesage, has not been
# defined. Python can't identify the variable name provided. A name error usually means we either forgot to set
# a variable's value before using it, or we made a spelling mistake when entering the variable's name.

# Of course, in this example we omitted the letter s in the variable name mesage in the second line. The Python
# interpreter doesn't spellcheck your code, but it does ensure that variable names are spelled consistently.

# Programming languages are strict, but they disregard good and bad spelling. As a result, you don't need to
# consider English spelling and grammar rules when you're trying to create variable names and writing code.

# Many programming errors are simple, single-character typos in one line of a program. If you're spending a long
# time searching for one of these errors, know that you're in good company. Many experienced and talented
# programmers spend hours hunting down these kinds of tiny errors. Try to laugh about it and move on, knowing
# it will happen frequently throughout your programming life.

message = "Hello Python Crash Course reader!"
print(mesage)
