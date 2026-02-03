# 37_dice.py

# 9-13. Dice: Make a class Die with one attribute called sides, which has a
# default value of 6. Write a method called roll_die() that prints a random
# number between 1 and the number of sides the die has. Make a 6-sided die and
# roll it 10 times.

# Make a 10-sided die and a 20-sided die. Roll each die 10 times.

from random import randint

class Die:
    """Represents a die."""

    def __init__(self, sides=6):
        """Initialize the sides attribute."""
        self.sides = sides

    def roll_die(self):
        """
        Prints a random number between 1 and the number of sides the die has.
        """
        print(randint(1, self.sides))

six_sided_die = Die()

print("6-sided die rolls:")
for n in range(10):
    six_sided_die.roll_die()

ten_sided_die = Die(10)
print("\n10-sided die rolls:")
for n in range(10):
    ten_sided_die.roll_die()

twenty_sided_die = Die(20)
print("\n20-sided die rolls:")
for n in range(10):
    twenty_sided_die.roll_die()
