# 23_privileges.py

# 9-8. Privileges: Write a seperate Privileges class. The class should have one
# attribute, privileges, that stores a list of strings as described in Exercise
# 9-7. Move the show_privileges() method to this class. Make a Privileges
# instance as an attribute in the Admin class. Create a new instance of Admin
# an use your method to show its privileges.


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

new_admin = Admin('Yeji', 'Hwang', 25, 167)
new_admin.privileges.show_privileges()
