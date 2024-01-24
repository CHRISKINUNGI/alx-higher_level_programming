#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is not None:
        dict_keys = sorted(a_dictionary.keys())
        for key in dict_keys:
            value = a_dictionary[key]
            print(f'{key}: {value}')
