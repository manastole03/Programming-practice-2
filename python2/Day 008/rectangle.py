# day 8
# (note : always take the input from the user, do not hard core the values)
#
# 1. Create class Rectangle which has attributes length and width. Create 2 methods for calculating area
# of rectangle and perimeter of rectangle.


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("The area of Rectangle: ", self.length * self.width)

    def perimeter(self):
        print("Perimeter of Rectangle: ", self.length + self.width)


l = float(input("Enter the length of rectangle: "))
w = float(input("Enter the width of rectangle: "))

rec1 = Rectangle(l, w)
rec2 = Rectangle(l, w)

rec1.area()
rec2.perimeter()



