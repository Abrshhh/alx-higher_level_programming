#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
y = int(number)
z = y % 10
x = f"Last digit of {number} is {z}"
if z > 5:
    print(f"{x} and is greater than 5")
elif z = 0:
    print(f"{x} and is 0")
else (z < 6) and (z != 0):
    print(f"{x} and is less than 6 and not 0")
