# Write a program that takes a number as input and prints its multiplication table upto 10.
# Test Data:
# Input a number: 8
# Expected Output :
# 8 x 1 = 8
# 8 x 2 = 16
# 8 x 3 = 24
# ...
# 8 x 10 = 80

number = int(input("Input a Number: "))
for i in range(1, 11):
    print("{0:<2} x {1:<2} = {2:<2}".format(number, i, number * i))

