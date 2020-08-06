# Python program to find the distance between two points in a 2D plane.
import math
def dist(p,q):
    distance = math.sqrt((p[0]-q[0])**2 + (p[1]-q[1])**2)
    print("The distance between the two points is ", distance)

x1,y1 = map(int,input("Please enter space seperated co-ordintes of first point:  ").split())
x2,y2 = map(int,input("Please enter space seperated co-ordintes of second point:  ").split())
p = (x1,y1)
q = (x2,y2)
dist(p,q)

while True:
    a = input("Do you want to calculate distance again? (Y or N):  ")
    if a == 'Y':
        x1,y1 = map(int,input("Please enter space seperated co-ordintes of first point:  ").split())
        x2,y2 = map(int,input("Please enter space seperated co-ordintes of second point:  ").split())
        p = (x1,y1)
        q = (x2,y2)
        dist(p,q)
    elif a == 'N':
        break
    else:
        print("Error!")
