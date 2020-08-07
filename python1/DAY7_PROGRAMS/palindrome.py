# Python function to check a palindrome.
def palindrome(string):
    print(string[::-1]==string)
string = input("Enter the string:  ")
palindrome(string)
while True:
    a  = input("Do you wnat to check a palindrome again? (Yes or No):  ")
    if a == 'Yes':
        string = input("Enter the string:  ")
        palindrome(string)
    elif a == 'No':
        break
    else:
        print("Enter 'Yes' or 'No'")
