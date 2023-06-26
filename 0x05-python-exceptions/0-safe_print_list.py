#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    _rtn = 0
    for y in range(x):
        try:
            print("{}".format(my_list[y]), end="")
            _rtn += 1
        except IndexError:
            break
        print("")
        return (_rtn)
