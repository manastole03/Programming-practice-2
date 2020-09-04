# 5. Use the decimal module to find the square root, exponent, natural log, fused multiply and add (fma)
# of two numbers. (do read about the "fma" before)

from decimal import *

num = eval(input("Enter the number:  "))
print("Square Root: ", Decimal(num).sqrt())
print("Exponent: ", Decimal(num).exp())
print("Natural log: ", Decimal(num).ln())
a = int(input())
b = int(input())
print("FMA: ", Decimal(num).fma(a, b))
