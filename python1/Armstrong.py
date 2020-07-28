# Python program to check if the number is an Armstrong number or not.
n = input()
a = list(n)
lst = []
for i in a:
    lst.append(int(i)**len(a))
if sum(lst) == int(n):
    print(f"{n} is an Armstrong number.")
else:
    print(f"{n} is not an Armstrong number.")

# Taking integer as input.
n = int(input())
a = str(n)
lst = []
for i in a:
    lst.append(int(i)**len(a))
if sum(lst) == int(n):
    print(f"{n} is an Armstrong number.")
else:
    print(f"{n} is not an Armstrong number.")
