# Class Rectangle
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        print("The area of rectangle is ",self.length*self.width,'sq units.')

    def perimeter(self):
        print("The perimeter of rectangle is ",2*(self.length+self.width),'units.')

l = float(input("Please enter the length of rectangle:  "))
w = float(input("Please enter the width of rectangle:  "))

r1 = Rectangle(l,w)
r2 = Rectangle(l,w)

r1.area()
r2.perimeter()
