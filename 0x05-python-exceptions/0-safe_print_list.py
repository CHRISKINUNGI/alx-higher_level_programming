#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    index = 0
    for count in range(x):
        try:
            print("{0}".format(my_list[count]), end="")
            index += 1
        except IndexError:
            break
        finally:
            print()

    return index
