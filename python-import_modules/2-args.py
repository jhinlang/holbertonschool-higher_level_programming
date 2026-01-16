#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv
    argc = len(argv) - 1

    if argc == 0:
        print("{} arguments.".format(argc)
    elif argc == 1:
        print("{} argument:".format(argc))
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(argc))
            for i in range(1, len(argv)):
                print("{} {}".format(i, argv[i]))
