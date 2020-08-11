# day 6
# 4. Write a program that asks the user to enter two points on a 2D plane
# (i.e. enter X1 & Y1,enter X2 & Y2). Compute the distance between those points using a function.


def distance():
    print("Input Point one: ")
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))
    dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    print("Distance: ", dist)


distance()