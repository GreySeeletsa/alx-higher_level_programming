#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    sum_of_all = 0
    for x in range(len(sys.argv) - 1):
        sum_of_all += int(sys.argv[x + 1])
    print("{}".format(sum_of_all))
