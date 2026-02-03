# 38_lottery.py

# 9-14. Lottery: Make a list or tuple containing a series of 10 numbers and five
# letters. Randomly select four numbers or letters from the list and print a
# message saying that any ticket matching these four numbers or letters wins a
# prize.

from random import choice

lucky_list = [
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E'
]

winning_ticket = []

for n in range(4):
    winning_ticket.append((choice(lucky_list)))

# Join the elements of winning_ticket into a single string for cleaner output
formatted_ticket = "".join(str(item) for item in winning_ticket)

print(f"The winning ticket is {formatted_ticket}.")
