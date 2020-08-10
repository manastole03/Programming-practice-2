# day 5
# 4.  Write a Python function to check whether a number is perfect or not.
# (read the concept of perfect number)

# A perfect number is a number which is equal to the sum of its proper positive divisors.
def perfect_number(num):
    add = 0
    for i in range(1, num):
        if num % i == 0:
            add += i
    if add == num:
        print(f"The {num} is a perfect number.")
    else:
        print(f"The {num} is not a perfect number.")


number = int(input("Enter a number to check: "))
perfect_number(number)
