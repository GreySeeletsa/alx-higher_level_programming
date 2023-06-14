#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    x = 0
    y = 0
    for tp in my_list:
        x += tp[0] * tp[1]
        y += tp[1]
    return (x / y)
