#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    k_list = list(a_dictionary.keys())
    for spec_val in k_list:
        if value == a_dictionary.get(spec_val):
            del a_dictionary[spec_val]
    return (a_dictionary)
