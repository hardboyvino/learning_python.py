class User():
    """Learning classes by creating a user's profile"""

    def __init__(self, first_name, last_name, nickname) -> None:
        """Creating the attributes of the user."""
        self.first_name = first_name
        self.last_name = last_name
        self.nickname = nickname

    def describe_user(self):
        """Printing all the attributes of the user."""
        print(f"The user {self.first_name.title()} {self.last_name.title()} has the nickname - {self.nickname}")

python_user = User("joey", "tribiani", "eater")

python_user.describe_user()