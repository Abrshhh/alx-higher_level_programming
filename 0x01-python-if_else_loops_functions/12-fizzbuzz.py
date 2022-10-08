#!/usr/bin/python3
def fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0:
            print("Bizz")
        elif number % 5 == 0:
            print("Buzz")
        elif number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        else:
            print("Not Fizz or Buzz")
