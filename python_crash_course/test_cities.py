import unittest
from city_functions import neat_city_name

class CitiesTest(unittest.TestCase):
    """Test the functions from city_functions.py"""

    def test_city_country(self):
        """Does the city, country return as City, Country?"""
        formated_city = neat_city_name("lagOs", "nigeRia")
        self.assertEqual(formated_city, "Lagos, Nigeria")

    def test_city_country_population(self):
        """Does the city, country return as City, Country?"""
        formated_city = neat_city_name("lagOs", "nigeRia", population=500)
        self.assertEqual(formated_city, "Lagos, Nigeria - population 500")

unittest.main()
