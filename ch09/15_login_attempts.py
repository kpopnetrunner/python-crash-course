# 15_login_attempts.py

# 9-5. Login Attempts: Add an attribute called login_attempts to your User class
# from Exercise 9-3 (page 162). Write a method called increment_login_attempts()
# that increments the value of login_attempts by 1. Write another method called
# reset_login_attempts() that resets the value of login_attempts to 0.

# Make an instance of the User class and call increment_login_attempts() several
# times. Print the vaue of login_attempts to make sure it was incremented
# properly, and then call reset_login_attempts(). Print login_attempts again to
# make sure it was reset to 0.

class User:
    """A simple attempt to model a user."""

    def __init__(self, first_name, last_name, age, height):
        """Initialize first_name, last_name, age, and height attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height
        self.login_attempts = 0

    def describe_user(self):
        """Prints user information."""
        print(f"{self.first_name.title()} {self.last_name.title()} "
        f"is {self.age} years old and has a height of {self.height} "
        f"centimeters.")

    def greet_user(self):
        """Prints a personalized greeting to the user."""
        print(f"Hello {self.first_name.title()} {self.last_name.title()}!")

    def increment_login_attempts(self):
        """Increments the value of login_attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets the value of login_attempts to 0."""
        self.login_attempts = 0

yeji = User('Yeji', 'Hwang', '25', '167')
yeji.increment_login_attempts()
print(yeji.login_attempts)
yeji.increment_login_attempts()
print(yeji.login_attempts)
yeji.increment_login_attempts()
print(yeji.login_attempts)
yeji.reset_login_attempts()
print(yeji.login_attempts)
