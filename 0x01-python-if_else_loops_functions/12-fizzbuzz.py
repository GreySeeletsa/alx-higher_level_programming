#!/usr/bin/python3
# function that prints the numbers from 1 to 100 separated by a space
def fizzbuzz():
    for numbers in range(1, 101):
        if numbers % 3 == 0 and numbers % 5 == 0:
            print('FizzBuzz', end='')
        elif numbers % 3 == 0:
            print('Fizz', end='')
        elif numbers % 5 == 0:
            print('Buzz', end='')
        else:
            print('{}'.format(numbers), end='')
