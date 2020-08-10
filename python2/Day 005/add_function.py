# day 5
# 1. Write a python program using function to add the given numbers.
# (numbers can be negative or positive, and no limit for the input numbers)

def addition():
    sum = 0
    while True:
        num = input("Enter number to add: ").lower()
        if num == 'q':
            break
        else:
            sum = sum + int(num)
            pass
    print("Sum of given numbers: ", sum)


print("NOTE: Press \"Q\" to exit!")
addition()
