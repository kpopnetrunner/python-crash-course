# 22_admin.py

# 9-7. Admin: An administrator is a special kind of user. Write a class called
# Admin that inherits from the User class you wrote in Exercise 9-3 (page 162)
# or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list
# of strings like "can add post", "can delete post", "can ban user", and so on.

# Write a method called show_privileges() that lists the administrator's set of
# privileges. Create an instance of Admin, and call your method.

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
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        """Displays the administrator's privileges."""
        print("Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

new_admin = Admin('Yeji', 'Hwang', 25, 167)
new_admin.show_privileges()

