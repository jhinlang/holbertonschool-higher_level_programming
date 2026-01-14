#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        end_char = "\n" if i == 100 else " "
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=end_char)
        elif i % 5 == 0:
            print("Buzz", end=end_char)
        elif i % 3 == 0:
            print("Fizz", end=end_char)
        else:
            print("{}".format(i), end=end_char)
    print()
