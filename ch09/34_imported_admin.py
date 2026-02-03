# 34_imported_admin.py

# 9-11. Imported Admin: Start with your work from Exercise 9-8 (page 173). Store
# the classes User, Privileges, and Admin in one module. Create a separate file,
# make an Admin instance, and call show_privileges() to show that everything is
# working correctly.

# admin_modules.py

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

class Admin(User):
    """Represents an administrator."""

    def __init__(self, first_name, last_name, age, height):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an administrator.
        """
        super().__init__(first_name, last_name, age, height)
        self.privileges = Privileges()

class Privileges:
    """Represents the privileges of an administrator."""

    def __init__(self):
        """Initialize the privileges attribute."""
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        """Displays the administrator's privleges."""
        print("Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

# my_admin.py

from admin_modules import User, Admin, Privileges

new_admin = Admin('Yeji', 'Hwang', 25, 167)
