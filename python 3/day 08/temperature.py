#conversion of c to f or f to c.py
class temperature:
    def __init__(self,c,f):
        self.c = c
        self.f = f
    def convertintoF(self):
        print("farenhait scale: ",(self.c - 32) * (5/9))
    def convertintoC(self):
        print("celcius scale: ",((9/5) *(self.f + 32))
x  = float(input("enter a number in celcius : "))   
y  = float(input("enter a number in farenhait : "))  

t1 = temperature(x,y)
t2 = temperature(x,y)

t1.convertintoF()
t2.convertintoC()
