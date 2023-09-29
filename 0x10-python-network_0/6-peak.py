#!/usr/bin/python3
""" Peak finding algorithm """


def find_peak(list_of_integers):
    """finds a peak in a list of integers
    Args:
    list_of_integers: list of integers
    Returns:
    The index of the peak in the list"""

    if len(list_of_integers) <= 1:
        return None

    list_len = len(list_of_integers)

    if list_len == 1:
        return list_of_integers[0]
    elif list_len == 2:
        return max(list_of_integers)

    mid = list_len // 2

    peak = list_of_integers[mid]

    if peak > list_of_integers[mid - 1] and peak > list_of_integers[mid + 1]:
        return peak

    elif peak < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
