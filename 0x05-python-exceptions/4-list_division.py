#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    if len(my_list_1) < list_length or len(my_list_2) < list_length:
        raise TypeError("out of range")
    elif not (type(my_list_1[i]) in (int, float)):
        raise TypeError("Wrong type")
    elif notnot (type(my_list_2[i]) in (int, float)):
        raise TypeError("Wrong type")

    for i in range(list_length):
        try:
            result = my_list_1[i]/my_list_2[i]
        except ValueError:
            result = 0
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            newlist[i] = result

    return newlist
