#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
num = number

if num < 0:
    i = ((-1 * num) % 10) * -1
else:
    i = num % 10


if i > 5:
    print("Last digit of {} is {} and is greater than 5".format(num, i))

elif i == 0:
    print("Last digit of {} is {} and is 0".format(num, i))

elif i < 6 and i != 0:
    print("Last digit of {} is {} and is less than 6 and not 0".format(num, i))
