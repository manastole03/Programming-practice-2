class point:
    def __init__(self,abssicca,ordinate,abssicca1,ordinate1):
        self.abssicca = abssicca
        self.ordinate = ordinate
        self.abssicca1 = abssicca1
        self.ordinate1 = ordinate1
    def showdisplay(self):
        print("first coordinate is of 1st point",self.abssicca)
        print("secind coordinate is 1st point",self.ordinate)
        print("first coordinate is 2nd point",self.abssicca1)
        print("secind coordinate is 2nd point",self.ordinate1)
    def distance(self):
        c = ((self.abssicca1 - self.abssicca)**2 + (self.ordinate1 - self.ordinate)**2)**(0.5)
        print(c)
a = int(input("enter the abssicca of first point : "))  
b = int(input("enter the ordinate of first point : "))  
f = int(input("enter the abssicca of second point : "))  
d = int(input("enter the ordinate of second point : ")) 

e = point(a,b,f,d)
e.showdisplay()
e.distance()
        
