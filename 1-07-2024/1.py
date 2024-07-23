#1. *Problem: Calculate Circle Area*
  # Write a Python program that asks the user for the radius of a circle and calculates its area. Print the area rounded to two decimal places.

import math

pi = 3.14
r = float(input("enter r:"))

a = math.pi * r * r

print(a)