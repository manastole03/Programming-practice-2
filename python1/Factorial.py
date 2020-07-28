# Python program for factorial of a given number.
n = int(input("Enter the number: "))
lst = []
for i in range(1,n+1):
    lst.append(i)
product = 1
for i in lst:
    product *= i
print(product)
