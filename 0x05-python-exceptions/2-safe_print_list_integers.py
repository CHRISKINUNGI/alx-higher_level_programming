#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    for count in my_list:
        while count < x:
            try:
                if my_list[count] is not int:
                    pass
                else:
                    print("{:d}".format(my_list(count), end=""))
                    count += 1
            except IndexError:
                pass
    print()
    return count
