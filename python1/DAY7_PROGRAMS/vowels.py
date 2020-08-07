# Python program to count vowels in user input.
def vowels():
    vowels = 0
    lst = ['a','e','i','o','u','A','E','I','O','U']
    user_input = input("Please enter the input string:  ")
    for i in user_input:
        if i in lst:
            vowels +=1
    print("Number of vowels in the string are: ",vowels)
vowels()
while True:
    a = input("Do you want to count vowels again? (Yes or No):  ")
    if a == 'Yes':
        vowels()
    elif a == 'No':
        break
    else:
        print("Please enter 'Yes' or 'No'")
