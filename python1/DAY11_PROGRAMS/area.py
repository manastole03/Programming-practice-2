# Python program to compute area
class Area():
    def __init__(self):
        self.length = None
        self.breadth = None

    def setDim(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def getArea(self):
        print("The area of the rectangle is : ",self.length*self.breadth)


l = float(input("Enter the length of rectangle:  "))
b = float(input("Enter the breadth of rectangle:  "))
a = Area()
a.setDim(l,b)
a.getArea()
