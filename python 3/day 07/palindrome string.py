def palindrome(strings):
    print(strings[::-1] = strings)
strings = input("Enter the string:  ")
palindrome(strings)
while True:
    a  = input("Do you wnat to check a palindrome again? (Yes or No):  ")
    if a == 'Yes':
        string = input("Enter the string:  ")
        palindrome(string)
    elif a == 'No':
        break
    else:
        print("Enter 'Yes' or 'No'")
