class Power:
    def __init__(self,x,n):
        self.x = x
        self.n = n

    def func_power(self):
        print(self.x ** self.n)

x = int(input("enter the first number:  "))
n = int(input("enter the second number:  "))

p = Power(x,n)
p.func_power()
