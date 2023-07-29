#!/usr/bin/python3

"""Module for load_from_json_file method"""

def load_from_json_file(filename):
    """Creates an Object from a “JSON file”"""
    import json
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
