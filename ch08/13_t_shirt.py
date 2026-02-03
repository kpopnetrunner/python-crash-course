# 13_t_shirt.py

# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
# text of a message that should be printed on the shirt. The function should
# print a sentence summarizing the size of the shirt and the message printed on
# it.

# Call the function once using positional arguments to make a shirt. Call the
# function a second time using keyword arguments.

def make_shirt(size, message):
  print(f"The shirt's size is {size.title()}.")
  print(f'The message on the shirt reads, "{message}"')

make_shirt('s', 'I like Python.')
make_shirt(size='m', message='I like C.')
