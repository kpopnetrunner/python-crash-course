# 33_imported_restaurant.py

# 9-10. Imported Restaurant: Using your latest Restaurant class, store it in a
# module. Make a separate file that imports Restaurant. Make a Restaurant
# instance, and call one of the Restaurant's methods to show that the import
# statement is working properly.

# restaurant_module.py

class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant_name and cuisine_type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Prints restaurant information."""
        print(f"This restaurant is called {self.restaurant_name.title()}, "
              f"and it serves {self.cuisine_type.title()} cuisine.")
    def open_restaurant(self):
        """Prints a message that the restaurant is open."""
        print(f"{self.restaurant_name.title()} is open.")
    def set_number_served(self, customers):
        """Sets the number of customers served."""
        self.number_served = customers
    def increment_number_served(self, customers):
        """Increments the number of customers served."""
        self.number_served += customers

# my_restaurant.py

from restaurant_module import Restaurant

my_restaurant = Restaurant('the best restaurant', 'italian')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
