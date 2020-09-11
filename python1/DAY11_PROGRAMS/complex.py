# Python program to perform operations on complex numbers

class Complex():
    def __init__(self, c1, c2):
        self.c1 = c1
        self.c2 = c2

    def sum(self):
        sum_real = self.c1[0] + self.c2[0]
        sum_imag = self.c1[1] + self.c2[1]
        print(f"The sum of two complex numbers is {sum_real} +({sum_imag})i")

    def difference(self):
        diff_real = self.c1[0] - self.c2[0]
        diff_imag = self.c1[1] - self.c2[1]
        print(f"The difference of two complex numbers is {diff_real} +({diff_imag})i")

    def product(self):
        pro_real = self.c1[0]*self.c2[0] - self.c1[1]*self.c2[1]
        pro_imag = self.c1[0]*self.c2[1] + self.c1[1]*self.c2[0]
        print(f"The product of two complex numbers is {pro_real} + ({pro_imag})i")


c1 = list(map(int, input("Enter the real and imaginary parts of first complex number:  ").split()))
c2 = list(map(int, input("Enter the real and imaginary parts of second complex number:  ").split()))
c = Complex(c1,c2)
c.sum()
c.difference()
c.product()
