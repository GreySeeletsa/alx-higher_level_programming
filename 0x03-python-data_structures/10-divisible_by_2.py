#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    multi = []
    for x in range(len(my_list)):
        if my_list[x] % 2 == 0:
            multi.append(True)
        else:
            multi.append(False)
    return (multi)
