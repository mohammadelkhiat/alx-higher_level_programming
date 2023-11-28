#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    LN = number % 10
else:
    LN = number % -10

if LN > 5:
    print(f"Last digit of {number} is {LN} and is greater than 5")
elif LN == 0:
    print(f"Last digit of {number} is {LN} and is 0")
else:
    print(f"Last digit of {number} is {LN} and is less than 6 and not 0")
