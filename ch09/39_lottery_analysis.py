# 39_lottery_analysis.py

# 9-15. Lottery Analysis: You can use a loop to see how hard it might be to win
# the kind of lottery you just modeled. Make a list or tuple called my_ticket.
# Write a loop that keeps pulling numbers until your ticket wins. Print a
# message reporting how many times the loop had to run to give you a winning
# ticket.

from random import choice

lucky_list = [
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E'
]

winning_ticket = ['C', 1, 8, 8]

my_ticket = []

count = 0

while my_ticket != winning_ticket:
    my_ticket = [] # Reset my_ticket for each attempt
    for n in range(4):
        my_ticket.append(choice(lucky_list))
    count += 1
    print(my_ticket)
    print(count)

print(f"It took {count} times to get a winning ticket.")
