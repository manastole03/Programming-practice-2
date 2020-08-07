# Python program to convert a decimal number to a binary number.
def decimal_binary(n):
    if n > 1:
        decimal_binary(n//2)
    print(n % 2, end='')
n = int(input("Enter the number:  "))
decimal_binary(n)
while True:
    a = input("\nDo you want to enter input again? (Yes or No):  ")
    if a == 'Yes':
        n = int(input("Enter the number:  "))
        decimal_binary(n)
    elif a =='No':
        break
    else:
        print("Error. Enter 'Yes' or 'No'")
