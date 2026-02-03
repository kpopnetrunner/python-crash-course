# 06_restaurant.py

# 9-1. Restaurant: Make a class called Restaurant. The __init__() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message
# indicating that the restaurant is open.

# Make an instance called restaurant from your class. Print the two attributes
# individually, and then call both methods.

class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant_name and cuisine_type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Prints restaurant information."""
        print(f"This restaurant is called {self.restaurant_name.title()}, "
              f"and it serves {self.cuisine_type.title()} cuisine.")
    def open_restaurant(self):
        """Prints a message that the restaurant is open."""
        print(f"{self.restaurant_name.title()} is open.")

restaurant = Restaurant('Chipotle', 'Mexican')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
