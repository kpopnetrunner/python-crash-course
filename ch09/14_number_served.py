# 14_number_served.py

# Page 167

# 9-4. Number Served: Start with your program from Exercise 9-1 (page 162).
# Add as an attribute called number_served with a default value of 0. Create
# an instance called restaurant from this class. Print the number of customers
# the restaurant has served, and then change the value and print it again.

# Add a method called set_number_served() that lets you set the number of
# customers that have been served. Call this method with a new number and print
# the value again.

# Add a method called increment_number_served() that lets you increment the
# number of customers who've been served. Call this method with any number you
# like that could represent how many customers were served in, say, a day of
# business.

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

restaurant = Restaurant('Chipotle', 'Mexican')
print(restaurant.number_served)
restaurant.number_served = 9
print(restaurant.number_served)

restaurant.set_number_served(10)
print(restaurant.number_served)

restaurant.increment_number_served(10)
print(restaurant.number_served)
