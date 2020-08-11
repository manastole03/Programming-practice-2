# day 6
# 1. Write a function that converts feet to inches.
# It should accept a number of feet as an argument and return the equivalent number of inches.
# Similarly for miles to kilometer, acre to square yards.

def feet_inch(f):
    inch = 12 * f
    print(f"{f} feet into inches: {inch} inch")


def miles_km(m):
    km = 1.60934 * m
    print(f"{m} miles into km: {km} km")


def acre_square_yard(a):
    square_yard = 4840 * a
    print(f"{a} acres into square yards: {square_yard} square yard")


feet = float(input("Enter no. of feet: "))
miles = float(input("Enter no. of miles: "))
acres = float(input("Enter no. of acres: "))

feet_inch(feet)
miles_km(miles)
acre_square_yard(acres)
