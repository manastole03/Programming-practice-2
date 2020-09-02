class car():
    def __init__(self,name,cost,colour,length):
        self.name = name
        self.cost = cost
        self.colour = colour
        self.length = length
        print("name :",self.name)
        print("cost :",self.cost)
        print("colour :",self.colour)
        print("length :",self.length)
    def disc(self):
        if(self.length > 4):
            print("you got a 10% discount!!\n")
            print("so your price is now",self.cost - self.cost*0.1)
            
string = input("enter a name : ")
c = int(input("enter the cost : "))
string1 = input("enter colour : ")
l = int(input("enter the length : "))

a = car(string,c,string1,l)
a.disc()
