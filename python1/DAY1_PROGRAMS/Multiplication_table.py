# Program to print multiplication table upto 10.
n = int(input("Enter the number: "))
while True:
    i = 1
    while i <=10:
        print("%d x %d = %d\n"%(n,i,n*i))
        i +=1
    break



i = 1
n = int(input())
for i in range(1,11):
    print("%d x %d = %d\n"%(n, i, n*i))
