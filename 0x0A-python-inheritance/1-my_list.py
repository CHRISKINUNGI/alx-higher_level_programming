#!/usr/bin/python3
"""
This module is about inheritance
"""


class MyList(list):
    """
    This class MyList is inheriting from list
    """

    def print_sorted(self):
        """
        This is a function of printing sorted integer values
        """
        print(sorted(self))
