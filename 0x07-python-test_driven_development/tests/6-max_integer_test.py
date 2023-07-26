#!/usr/bin/python3

import unittest
max_integer = __import__('6-max_integer').max_integer
"""Tests for the function max_integer which returns the largest integer
	in a list of integers and if the list is empty it returns NULL"""


class MaxIntegerTest(unittest.TestCase):
    """Definig a class for my tests"""

    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        """Tests ordered list"""

    def test_unordered_list(self):
        "Tests for a jungled up list"
        self.assertEqual(max_integer([2, 6, 8, 4]), 8)

    def test_negative_numbers(self):
        """"Tests among negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_types(self):
        """Tests among mixed data types"""
        self.assertEqual(max_integer([3.5, 4, 19.0, 3]), 19.0)

    def test_equal_list(self):
        """Checks for a list of equal values"""
        self.assertEqual(max_integer([1, 1, 1]), 1)

    def test_one_element(self):
        """checks in a list of one element"""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Checks for an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_empty_string(self):
        """Checks an empty string"""
        self.assertEqual(max_integer(""), None)

    def test_string(self):
        """checks a string"""
        self.assertEqual("BAD Boys", 'y')

    def test_string_list(self):
        """checks in a mixed up list"""
        self.assertEqual(max_integer(
            ["Today", "is", "a", "good", "day"], 'is'))


if __name__ == '__main__':
    unittest.main()
