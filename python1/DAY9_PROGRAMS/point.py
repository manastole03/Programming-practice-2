# Python class Point.
class Point():
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def show(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        print(f"The co-ordinates of the points are {(x1,y1)} and {(x2,y2)} respectively.")

    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        print("The distance between the two points is ",((x1-x2)**2+(y1-y2)**2)**0.5,"units.")
x1 = eval(input("Enter the x-coordinate of first point:  "))
y1 = eval(input("Enter the y-coordinate of first point:  "))
x2 = eval(input("Enter the x-coordinate of second point:  "))
y2 = eval(input("Enter the y-coordinate of second point:  "))

coordinate1 = (x1,y1)
coordinate2 = (x2,y2)

p = Point(coordinate1,coordinate2)
p.show()
p.distance()
