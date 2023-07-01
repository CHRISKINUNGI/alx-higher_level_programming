#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    for i in range(list_length):
        try:
            result = my_list_1[i]/my_list_2[i]
            if not type(my_list_1[i]) and type(my_list_2[i]) is int or float:
                print("Wrong type")
        except ValueError:
            result = 0
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            newlist[i] = result

    return newlist
