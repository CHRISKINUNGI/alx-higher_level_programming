#!/usr/bin/python3
def uppercase(str):
    for i in str:

        """ checks if its ASCII value range (97 to 122) is lower. """
        if ord(i) >= 97 and ord(i) <= 122:

            """ converts to uppercase """
            i = chr(ord(i) - 32)
        print("{}".format(i), end="")
    print()
