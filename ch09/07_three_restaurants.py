# 07_three_restaurants.py

# 9-2. THree Restaurants: Start with your class from Exercise 9-1. Create three
# different instances from the class, and call describe_restaurant() for each
# instance.

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

restaurant_1 = Restaurant('Chipotle', 'Mexican')
restaurant_2 = Restaurant('McDonalds', 'American')
restaurant_3 = Restaurant('Panda Express', 'Chinese')

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()
