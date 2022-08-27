import unittest
from seasons import get_birthday, calculate_date_difference


class SeasonsTestCases(unittest.TestCase):
    """Test all the functions in seasons.py"""

    def test_get_birthday(self):
        """Does birthday 1900-01-12 work?"""
        birthday = get_birthday()
        self.assertEqual(birthday, "1900-01-12 00:00:00")

    def test_calculate_minutes(self):
        """Does the date 1900-01-12 give 64491840 minutes?"""
        minutes_since_birth = calculate_date_difference()
        self.assertEqual(minutes_since_birth, 64491840)


unittest.main()
