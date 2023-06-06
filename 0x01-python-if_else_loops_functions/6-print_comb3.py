#!/usr/bin/python3
# this program prints all possible different combinations of 2 digits
for numbers1 in range(0, 10):
    for numbers2 in range(numbers1 + 1, 10):
        if numbers1 == 8 and numbers2 == 9:
            print('{}{}'.format(numbers1, numbers2))
        else:
            print('{}{}'.format(numbers1, numbers2), end=', ')
