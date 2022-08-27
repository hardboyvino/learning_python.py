class IceCreamStand:
    """Class describing restaurant flavours. Never mind the name."""

    def __init__(self, flavours) -> None:
        """Initialize the flavours class"""
        self.flavours = flavours

    def describe_flavour(self):
        """Describe the flavours available"""
        print("These are the flavours served: ")
        for flavour in self.flavours:
            print(f"- {flavour}")


class Restaurant:
    """Testing how to make classes using restaurant"""

    def __init__(self, name, cuisine_type, flavours) -> None:
        """Describe the attributes of the restaurant"""
        self.name = name
        self.cuisine_type = cuisine_type
        self.flavours = IceCreamStand(flavours)

    def describe_restaurant(self):
        print(f"{self.name.title()} serves {self.cuisine_type.title()} dishes")

    def open_restaurant(self):
        print(f"{self.name.title()} is open for business!")


food = Restaurant("metro cafe", "italian", ["vanilla", "strawberry"])
print(f"{food.name.title()} - {food.cuisine_type.title()}")

food.describe_restaurant()
food.open_restaurant()
food.flavours.describe_flavour()
