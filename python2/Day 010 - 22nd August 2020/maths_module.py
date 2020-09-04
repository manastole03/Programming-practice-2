# 1.  Write a python program to print the square root, degrees, radians, sin,
# cos, tan, factorial, gamma function, log (of base 10) of a given number.

import math

num = eval(input("Enter the number:  "))
print("Square root : ", math.sqrt(num))
print("Degrees : ", math.degrees(num))
print("Radians : ", math.radians(num))
print("Sin : ", math.sin(num))
print("Cosine : ", math.cos(num))
print("Tangent : ", math.factorial(num))
print("Gamma function : ", math.gamma(num))
print("Logarithmic function : ", math.log(num, 10))
