#!/usr/bin/python3
def uppercase(str):
    for i in str:

        # checks if its ASCII value falls within the range of lowercase letters (97 to 122).
        if ord(i) >= 97 and ord(i) <= 122:

         #converts to uppercase   
            i = chr(ord(i) - 32)
        print("{}".format(i), end="")
    print()
