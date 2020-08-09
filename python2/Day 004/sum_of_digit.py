# 4) Calculate the sum of digits of a number given by user. E.g.-
#    INPUT : 123        OUTPUT : 6
#    INPUT : 12345      OUTPUT : 15

num = int(input("Enter the number: "))
sum = 0
while num > 0:
    remainder = num % 10
    sum = sum + remainder
    num = num//10

print("Sum of digits of number is ", sum)
