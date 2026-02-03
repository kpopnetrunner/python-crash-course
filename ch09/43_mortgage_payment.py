# 43_mortage_payment.py

"""An attempt to calculate a monthly mortgage payment."""

class MortgagePayment():
    """An attempt to calculate a monthly mortgage payment."""

    def __init__(self, principal, rate, years, property_taxes, insurance):
        """
        Initialize principle, rate, years, property_taxes, and insurance
        attributes.
        """
        self.principal = principal
        self.rate = rate
        self.years = years
        self.property_taxes = property_taxes
        self.insurance = insurance

    def calculate_payment(self):
        """Calculate and return the monthly payment."""
        r = self.rate / 12
        n = self.years * 12
        numerator = r * (1 + r) ** n
        denominator = (1 + r) ** n - 1
        payment = self.principal * (numerator / denominator)
        monthly_property_taxes = self.property_taxes / 12
        monthly_insurance = self.insurance / 12
        total_payment = payment + monthly_property_taxes + monthly_insurance
        return total_payment

class GetInput:
    """An attempt to get user input."""

    def __init__(self):
        """
        Initialize principal, rate, years, property_taxes, and insurance
        attributes.
        """
        self.principal = 0.0
        self.rate = 0.0
        self.years = 0.0
        self.property_taxes = 0.0
        self.insurance = 0.0

    def get_input(self):
        """Get user input for principal, rate, and years."""
        self.principal = float(input("Enter the principal amount: "))
        self.rate = float(input("Enter the annual interest rate (ex: 0.08):"))
        self.years = float(input("Enter the number of years: "))
        self.property_taxes = float(input("Enter the annual property taxes: "))
        self.insurance = float(input("Enter the annual insurance amount: "))

# Create an instance of GetInput and get user input.
user_input = GetInput()
user_input.get_input()

# Create an instance of MortgagePayment using the values from user_input.
mortgage_calculator = MortgagePayment(
    user_input.principal,
    user_input.rate,
    user_input.years,
    user_input.property_taxes,
    user_input.insurance
)

# Calculate and print the monthly mortage payment.
monthly_payment = mortgage_calculator.calculate_payment()
print(f"The monthly mortgage payment is {monthly_payment:.2f}.")
