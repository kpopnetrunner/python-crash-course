# One kind of error that you might see with some regularity is a syntax error. A syntax error occurs when Python
# doesn't recognize a section of your program as valid Python code. For example, if you use an apostrophe within
# single quotes, you'll produce an error. This happens because Python interprets everything between the first
# single quote and the apostrophe as a string. It then tries to interpret the rest of the text as Python code,
# which causes errors.

# Here's how to use single and double quotes correctly. Save this program as apostrophe.py and then run it:
# message = "One of Python's strengths is its diverse community."
# print(message)

# The apostrophe appears inside a set of double quotes, so the Python interpreter has no trouble reading the
# string correctly:

# One of Python's strengths is its diverse community.

# However, if you use single quotes, Python can't identify where the string should end:

# message = 'One of Python's strengths is its diverse community.'
# print(message)

# You'll see the following output:

# File "apostrophe.py", line 1
#   message = 'One of Python's strenths is its diverse community.'
# SyntaxError: invalid syntax

# In the output you can see that the error occurs at 1 right after the second single quote. This syntax error indicates
# that the interpreter doesn't recognize something in the code as valid Python code. Errors can come from a variety of
# sources, and I'll point out some common ones as they arise. You might see syntax errors often as you learn to write
# proper Python code. Syntax errors are also the least specific kind of error, so they can be difficult and frustrating
# to identify and correct. If you get stuck on a particularly stubborn error, see the suggestions in Appendix C.

# NOTE

# Your editor's syntax highlighting feature should help you spot some syntax errors quickly as you write your programs.
# If you see Python code highlighted as if it's English or English highlighted as if it's Python code, you probably have
# a mismatched quotation mark somewhere in your file.

print("This program contains notes in the comments.")
