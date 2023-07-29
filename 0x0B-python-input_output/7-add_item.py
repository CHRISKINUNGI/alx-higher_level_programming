#!/usr/bin/python3

"""Add item module"""

def add_item(args):
    """Adds all arguments to a Python list, and then save them to a file"""
    with open("add_item.json", "a") as f:
	    f.write(args)
