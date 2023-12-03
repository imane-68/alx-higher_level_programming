#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    i = len(sys.argv) - 1
    if i == 0:
        print("0 arguments.")
    elif i == 1:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(i))
    for x in range(i):
        print("{}: {}".format(x + 1, sys.argv[x + 1]))
