# Python program to print list of squares of given numbers
def squares(n):
    lst = []
    for i in n:
        lst.append(i**2)
    print(lst)

n = list(map(int, input("Please enter the space seperated numbers.").split()))
squares(n)
