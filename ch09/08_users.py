# 08_users.py

# 9-3. Users: Make a class called User. Create two attributes called first_name
# and last_name, and then creat eseveral other attributes that are typically
# stored in a user profile. Make a method called describe_user() that prints
# a summary of the user's information. Make another method called greet_user()
# that prints a personalized greeting to the user.

# Create several instances representing different users, and call both methods
# for each user.

class User:
    """A simple attempt to model a user."""

    def __init__(self, first_name, last_name, age, height):
        """Initialize first_name, last_name, age, and height attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height

    def describe_user(self):
        """Prints user information."""
        print(f"{self.first_name.title()} {self.last_name.title()} "
        f"is {self.age} years old and has a height of {self.height} "
        f"centimeters.")

    def greet_user(self):
        """Prints a personalized greeting to the user."""
        print(f"Hello {self.first_name.title()} {self.last_name.title()}!")

yeji = User('Yeji', 'Hwang', '25', '167')
lia = User('Jisu', 'Choi', '25', '163')
ryujin = User('Ryujin', 'Shin', '24', '164')
chaeryeong = User('Chaeryeong', 'Lee', '24', '166')
yuna = User('Yuna', 'Shin', '22', '170')

yeji.describe_user()
yeji.greet_user()
lia.describe_user()
lia.greet_user()
ryujin.describe_user()
ryujin.greet_user()
chaeryeong.describe_user()
chaeryeong.greet_user()
yuna.describe_user()
yuna.greet_user()
