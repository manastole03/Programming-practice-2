def area(a,b):
    c = a*b
    print("area of rectangle is",c)
    
def perimeter(a,b):
    d = 2*a+2*b
    print("perimeter of rectangle is",d)
    
x = int(input("enter length : "))  
y = int(input("enter width : "))  

print("enter 1 for area and enter 2 for perimeter")
n = int(input("enter choice 1 or 2 : "))
if( n == 1):
    area(x,y)
elif(n == 2):
    perimeter(x,y)
else:
    print("you entered wrong choice.sorry!")
