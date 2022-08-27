class Restaurant():
    """Testing how to make classes using restaurant"""

    def __init__(self, name, cuisine_type) -> None:
        """Describe the attributes of the restaurant"""
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.name.title()} serves {self.cuisine_type.title()} dishes")

    def open_restaurant(self):
        print(f"{self.name.title()} is open for business!")


food = Restaurant("metro cafe", "italian")
print(f"{food.name.title()} - {food.cuisine_type.title()}")

food.describe_restaurant()
food.open_restaurant()
