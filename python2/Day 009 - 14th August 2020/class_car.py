# Day 9
# 1. Write a python program to create class car with attributes name, cost, colour, length.
# If the length>4m,
# discount=10%. Display the information of the car.

class Car:
    def __init__(self, n, co, col, ll):
        self.n = n
        self.co = co
        self.col = col
        self.ll = ll

    def information(self):
        if self.ll > 4:
            self.co = self.co - (self.co * 0.1)
            print("Name: ", self.n)
            print("Cost: ", self.co)
            print("Colour: ", self.col)
            print("Length: ", self.ll)
        else:
            print("Name: ", self.n)
            print("Cost: ", self.co)
            print("Colour: ", self.col)
            print("Length: ", self.ll)


name = input("Enter the name: ")
cost = float(input("Enter the cost: "))
colour = input("Enter the colour:")
length = int(input("Enter length in meters: "))

ob1 = Car(name, cost, colour, length)

ob1.information()
