# Python program to calculate the sum of digits of a number given by user.
nums = int(input("Please enter the number:  "))
a = str(nums)
lst = []
for i in a:
    lst.append(eval(i))
print(sum(lst))
