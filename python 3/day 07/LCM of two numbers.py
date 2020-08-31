def gcd(a,b):
    if a == 0:
        return b
    return gcd(b % a , a)

def lcm(a,b):
    print((a*b)/gcd(a,b))

a = float(input("Please enter the first number:  "))
b = float(input("Please enter the second number:  "))
print(lcm(a,b))

while True:
    c = input("Do you want to calculate LCM again? (yes or no):  ")
    if c == 'yes':
        a= float(input("Please enter the first number:  "))
        b = float(input("Please enter the second number:  "))
        print(lcm(a,b))
    elif c == 'no':
        break
    else:
        print("Enter 'yes' or 'no' ")
