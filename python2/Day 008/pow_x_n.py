# day 8
# pow(x,n) that returns x in power n
#
# 3. Write a Python class to implement pow(x, n).

class Power:
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def pow(self):
        print(self.p ** self.q)


x = int(input("Enter the value of x: "))
n = int(input("Enter the value of n: "))

p1 = Power(x, n)
p1.pow()

