#!/usr/bin/python3

class MyList(list):
    """ Class that inherits from list """
    def print_sorted(self):
        """ Function that prints the list, but sorted (ascending sort) """
        print(sorted(self))
