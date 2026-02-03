# 42_compound_interest.py

"""
This program calculates compound interest using the formula A = P(1 + r/n)^nt,
using the CompoundIntereset and GetInput classes.
"""

class CompoundInterest:
    """An attempt to calculate compound interest."""

    def __init__(self, principal, rate, periods, time):
        """Initialize principal, rate, periods, and time attributes."""
        self.principal = principal
        self.rate = rate
        self.periods = periods
        self.time = time

    def calculate_interest(self):
        base = 1 + (self.rate / self.periods)
        exponent = self.periods * self.time
        amount = self.principal * (base ** exponent)
        return amount

class GetInput:
    """An attempt to get user input."""

    def __init__(self):
        """Initialize principal, rate, periods, and time attributes."""
        self.principal = 0.0
        self.rate = 0.0
        self.periods = 0.0
        self.time = 0.0

    def get_input(self):
        """Get user input for principal, rate, periods, and time."""
        self.principal = float(input("Enter the principal amount: "))
        self.rate = float(input("Enter the annual interest rate (ex: 0.08): "))
        self.periods = float(input("Enter the number of periods per year (ex: 1): "))
        self.time = float(input("Enter the number of years: "))

# Create an instance of GetInput and get user input.
user_input = GetInput()
user_input.get_input()

# Create an instance of CompoundInterest using the values from user_input.
compound_calculator = CompoundInterest(
    user_input.principal,
    user_input.rate,
    user_input.periods,
    user_input.time
)

# Calculate and print the interest.
final_amount = compound_calculator.calculate_interest()
print(f"The final amount after compounding interest is: {final_amount:.2f}")
