#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    new_list = list(set(my_list))

    for element in range(0, len(new_list)):
        total = total + new_list[element]
    return total
