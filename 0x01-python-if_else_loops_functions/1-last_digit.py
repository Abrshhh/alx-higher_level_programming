#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
y = f"{number % 10}"
x = f"Last digit of {number} is {y}"
if f"{y}" > 5:
    print(f"{x} and is greater than 5")
elif f"{y}" = 0:
    print(f"{x} and is 0")
else (f"{y}" < 6) and (f"{y}" != 0):
    print(f"{x} and is less than 6 and not 0")
