#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    order = list(a_dictionary.keys())
    order.sort()
    for x in order:
        print("{}: {}".format(x, a_dictionary.get(x)))
