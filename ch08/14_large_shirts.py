# 14_large_shirts.py

# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
# by default with a message that reads I love Python. Make a large shirt and a
# medium shirt with the default message, and a shirt of any size with a
# different message.

def make_shirt(size='l', message='I love Python.'):
  print(f"The shirt's size is {size.title()}.")
  print(f'The message on the shirt reads, "{message}"')

make_shirt()
make_shirt('m')
make_shirt('s', 'I prefer C.')
