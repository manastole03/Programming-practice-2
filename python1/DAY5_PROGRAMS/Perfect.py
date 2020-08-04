# Python program to check whether the number is perfect or not.
def perfect(n):
    total = 0
    for i in range(1,n):
        if n%i == 0:
            total +=i
    if n == total:
        print("The number is a perfect number.")
    else:
        print("The number is not a perfect number.")
n = int(input("Please enter the number:  "))
perfect(n)
