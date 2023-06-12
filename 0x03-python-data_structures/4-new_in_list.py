#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    my_list1 = my_list[:]
    if idx < 0:
        return my_list1
    elif idx >= len(my_list):
        return my_list1
    else:
        my_list1[idx] = element
        return my_list1
