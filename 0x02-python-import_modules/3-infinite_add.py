#!/usr/bin/python3
import sys

if __name__ == "__main__":
    sum = 0
    for i in range(len(sys.argv) - 1):
        sum += int(sys.argv[i+1])
    print("{}".format(sum))
