# Python program to return the greater number.
def greater(a,b):
    if a>b:
        print(f'{a} is greater than {b}')
    else:
        print(f'{b} is greater than {a}')
a = int(input())
b = int(input())
greater(a,b)

# Python program to return the smaller number.
def smaller(a,b):
    if a<b:
        print(f'{a} is smaller than {b}')
    else:
        print(f'{b} is smaller than {a}')
a = int(input())
b = int(input())
smaller(a,b)
