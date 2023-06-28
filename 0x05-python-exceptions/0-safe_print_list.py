#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    index = 0
    for count in range(x):
        try:
            print("{}".format(my_list[count]), end=" ")
            index += 1
        except IndexError:
            break
    print()
    return index + 1
