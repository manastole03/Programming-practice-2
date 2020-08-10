# day 5
# 5. Define a function which can generate and print a list where the values
# are square of numbers (numbers taken from user)

def square():
    list = []
    while True:
        number = input("Enter number: ").lower()
        if number == 'q':
            break
        else:
            num = int(number)
            list.append(num ** 2)
    print(list)


print("NOte: Press 'q' to exit")
square()

