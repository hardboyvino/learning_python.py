class Restaurant():
    """Testing how to make classes using restaurant"""

    def __init__(self, name, cuisine_type) -> None:
        """Describe the attributes of the restaurant"""
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.name.title()} serves {self.cuisine_type.title()} dishes")

    def open_restaurant(self):
        print(f"{self.name.title()} is open for business!")

    def restaurant_orders(self):
        print(f"The number of orders are {self.number_served}")
    
    def set_number_served(self):
        self.number_served = 5

    def increment_number_served(self, orders):
        """Increase the number of served by orders recieved"""
        self.number_served += orders

class OnlineRestaurant(Restaurant):
    def __init__(self, name, cuisine_type) -> None:
        super().__init__(name, cuisine_type)
        

restaurant = Restaurant("metro cafe", "italian")
online_order = OnlineRestaurant("papies mastro", "junk food", "breakfast")

restaurant.set_number_served()
restaurant.restaurant_orders()
restaurant.increment_number_served(50)
restaurant.restaurant_orders()
print()
restaurant.describe_restaurant()
online_order.describe_restaurant()

