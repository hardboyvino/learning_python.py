class Car():
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """A finely printed description of the car."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=70) -> None:
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            car_range = 240
        elif self.battery_size == 85:
            car_range = 270

        print(f"This car can go approximately {car_range} miles on a full charge.")

    def upgrade_battery(self):
        """Suggest a battery upgrade if the range is not far enough."""
        self.battery_size = 85


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialise the attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()

# # --- CREATE A CAR INSTANCE --- #
# my_tesla = ElectricCar('tesla', 'model s', 2016)

# # --- DESCRIBE THE TESLA --- #
# print(my_tesla.get_descriptive_name())

# # --- DESCRIBE THE BATTERY kWh --- #
# my_tesla.battery.describe_battery()

# # ---  GET THE RANGE BEFORE ANY UPGRADE --- #
# my_tesla.battery.get_range()

# # --- UPGRADE THE TESLA BATTERY --- #
# my_tesla.battery.upgrade_battery()

# # --- GET THE NEW RANGE AFTER UPGRADE --- #
# my_tesla.battery.get_range()
