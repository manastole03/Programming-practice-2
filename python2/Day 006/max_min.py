# day 6
# 2. Write a function named “maximum”and "minimum" that accepts two integer values
# and returns the one that the greater or smaller of the two to the calling program.

def min_max(num1, num2):
    if num1 > num2:
        print("Maximum: ", num1)
        print("Minimum: ", num2)
    elif num1 < num2:
        print("Maximum: ", num2)
        print("Minimum: ", num1)
    else:
        print(f"{num1} == {num2}")


n1 = float(input("Enter num1: "))
n2 = float(input("Enter num2: "))
min_max(n1, n2)

