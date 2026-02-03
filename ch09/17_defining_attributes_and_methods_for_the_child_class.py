# 17_defining_attributes_and_methods_for_the_child_class.py

# Once you have a child class that inherits from a parent class, you can add any
# new attributes and methods necessary to differentiate the child class from the
# parent class.

# Let's add an attribute that's specific to electric cars (a battery,
# for example) and a method to report on this attribute. We'll store the battery
# size and write a method that prints a description of the battery:


# You don't always have to start from scratch when writing a class. If the class
# you're writing is a specialized version of another class you wrote, you can
# use inheritance. When one class inherits from another, it takes on the
# attributes and methods of the first class. The original class is called the
# parent class, and the new class is the child class. The child class can
# inherit any or all of the attributes and methods of its paraent class, but
# it's also free to define new attributes and methods of its own.

# The __init__() Method for a Child Class

# When you're writing a new class based on an existing class, you'll often want
# to call the __init__() method from the parent class. This will initialize any
# attributes that were defined in the parent __init__() method and make them
# available in the child class.

# As an example, let's model an electric car. An electric car is just a specific
# kind of car, so we can base our new ElectricCar class on the Car class we
# wrote earlier. Then we'll only have to wrie code for the attributes and
# behavior specific to electric cars.

# Let's start by making a simple version of the ElectricCar class, which does
# everything the Car class does:

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initinalize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 75                                                #1

    def describe_battery(self):                                               #2
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

# At 1 we add a new attribute self.battery_size and set its inital value to, say
# , 75. This attribute will be associated with all instances created from the
# ElectricCar class but won't be associated with any instances of Car. We also
# add a method called describe_battery() that prints information about the
# battery at 2. When we call this method, we get a description that is clearly
# specific to an electric car:

# 2019 Tesla Model S
# This car has a 75-kWh battery.

# There's no limit to how much you can specialize the ElectricCar class. You can
# add as many attributes and methods as you need to model an electric car to
# whatever degree of accuracy you need. An attribute or method that could belong
# to any car, rather than one that's specific to an electric car, should be
# added to the Car class instead of the ElectricCar class. Then anyone who uses
# the Car class will have that functionality available as well, behavior
# specific to electric vehicles.
