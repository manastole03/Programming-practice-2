# Python class Car.
class Car():
    def __init__(self,name,cost,colour,length):
        self.name = name
        self.cost = cost
        self.colour = colour
        self.length = length
        print("The name of the car is ",self.name)
        print("The cost of the car is $",self.cost)
        print("The colour of the car is" ,self.colour)
        print("The length of the car is ",self.length)
    def discount(self):
        if self.length >4:
            print("The discounted price of the car is ",self.cost-(self.cost*10/100))
name = input("Enter the name of the car:  ")
cost = int(input("Enter the cost of the car:  "))
colour = input("Enter the colour of the car:  ")
length = int(input("Enter the length of the car:  "))
c = Car(name,cost,colour,length)
c.discount()
