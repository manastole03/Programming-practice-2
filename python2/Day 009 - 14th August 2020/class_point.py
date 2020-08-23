# day 9
# 2. Write the definition of a Point class. Objects from this class should have
# i. A method show to display the coordinates of the point
# ii. A method dist that computes the distance between 2 points.

class Point:
    def __init__(self, c1, c2, c3, c4):
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.c4 = c4

    def display(self):
        print(f"P1: ({self.c1}, {self.c3})")
        print(f"P2: ({self.c2}, {self.c4})")

    def dist(self):
        d = (((self.c1 - self.c2)**2) + ((self.c3 - self.c4)**2)) ** 0.5
        print(f"Distance: {d}")


print("Enter co-ordinates of Point1: ")
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
print("Enter co-ordinates of Point2: ")
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

ans = Point(x1, x2, y1, y2)

# 1
ans.display()
# 2
ans.dist()