# Python class to implement pow.
class Pow:
    def __init__(self,x,n):
        self.x = x
        self.n = n

    def func_pow(self):
        print(self.x ** self.n)

x = int(input("enter the first number:  "))
n = int(input("enter the second number:  "))

p = Pow(x,n)
p.func_pow()
