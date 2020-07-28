# Python program that accepts an integer(n) and computes the value of n+nn+nnn.
n = int(input("Enter the number: "))
a = n +(10*n+n) + (n*100+10*n+n)
print(a)
