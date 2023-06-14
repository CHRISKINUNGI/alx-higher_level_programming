#!/usr/bin/python3
import sys
 if _name_ == "_main_":
     sum = 0
     for i in range(len(sys.argv) - 1):
         sum += int(sys.argv[i + 1])
     print("{}".format(sum))
