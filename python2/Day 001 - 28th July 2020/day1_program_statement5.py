# Write a program to swap two variables.
# i)using three variable.

var1 = 8
var2 = 4
temp = None

print("Before Swapping: ")
print("var1 : ", var1, "and var2 : ", var2)
temp = var1
var1 = var2
var2 = temp

print("[three variables: ]After Swapping: ")
print("var1 : ", var1, "and var2 : ", var2)

# ii. using 2 variables
# Hint : The idea is to get sum in one of the two given numbers.
# The numbers can then be swapped using the sum and subtraction from sum.
var1 = var1 + var2
var2 = var1 - var2
var1 = var1 - var2
print()
print("[two variables: ]After Swapping: ")
print("var1 : ", var1, "and var2 : ", var2)
