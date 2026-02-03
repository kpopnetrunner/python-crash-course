# 21_ice_cream_stand.py

# 9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant.
# Write a class called IceCreamStand that inherits from the Restaurant class you
# wrote in Exercise 9-1 (page 162) or Exercise 9-4 (page 167). Either version
# of the class will work; just pick the one you like better. Add an attribute
# called flavors that stores a list of ice cream flavors. Write a method that
# displays these flavors. Create an instance of IceCreamStand, and call this
# method.

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

class IceCreamStand(Restaurant):
    """Represents an ice cream stand."""

    def __init__(self, restaurant_name, cuisine_type):
        """
        Initialize attributes of the parent class.
        The initialize attributes specific to an ice cream stand.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'strawberry']

    def display_flavors(self):
        """Displays the available flavors."""
        print("Available flavors:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")

my_ice_cream_stand = IceCreamStand('My Ice Cream Stand', 'Ice Cream')
my_ice_cream_stand.display_flavors()
