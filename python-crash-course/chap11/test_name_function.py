import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Ned Flanders' work?"""
        formatted_name = get_formatted_name('ned', 'flanders')
        self.assertEqual(formatted_name, 'Ned Flanders')

    def test_first_last_middle_name(self):
        """Do names like 'Charles Montgomery Burns' work?"""
        formatted_name = get_formatted_name('charles', 'burns', 'montgomery')
        self.assertEqual(formatted_name, 'Charles Montgomery Burns')

unittest.main()