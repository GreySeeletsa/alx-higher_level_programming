#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    nlist = []
    for y in range(0, list_length):
        try:
            divide = my_list_1[y] / my_list_2[y]
        except TypeError:
            print("wrong type")
            divide = 0
        except ZeroDivisionError:
            print("division by 0")
            divide = 0
        except IndexError:
            print("out of range")
            divide = 0
        finally:
            nlist.append(divide)
    return (nlist)
