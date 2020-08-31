def count():
    v = 0
    list =['a','e','i','o','u','A','E','I','O','U']
    str = input("enter a string : ")
    for i in list:
        if i in str:
            v += 1
    print("so,the vowels in th given string are",v)
count()    

while True:
    a = input("Do you want to count vowels again? (Yes or No):  ")
    if a == 'Yes':
        count()
    elif a == 'No':
        break
    else:
        print("Please enter 'Yes' or 'No'")
