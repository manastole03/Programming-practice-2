# Python program to compute area and perimeter of triangle

class Triangle():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        semi = (self.a+self.b+self.c)/2
        area_of_triangle = (semi*(semi-self.a)*(semi-self.b)*(semi-self.c))**0.5
        print("The area of triangle is : ", area_of_triangle, "sq units")

    def perimeter(self):
        peri_of_tri = self.a+self.b+self.c
        print("The perimeter of triangle is : ", peri_of_tri, "units")

triangle = Triangle(3,4,5)
triangle.area()
triangle.perimeter()
