# Star-Underscore pattern
n = int(input())
print('*'*n,end='\n')
i = n//2 - 1
j = 2
while i!=0:
    while j <=(n - 2):
        print("*"*i, end="")
        print("_"*j, end="")
        print("*"*i,end='\n')
        i-=1
        j+=2
