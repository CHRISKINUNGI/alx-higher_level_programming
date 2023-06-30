#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    for count in range(x):
        try:
            print("{:d}".format(my_list(count), end=""))
            counter += 1
        except (IndexError, ValueError):
            pass
    print()
    return counter
