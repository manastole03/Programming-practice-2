def biodata(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)
        
a=int(input("enter the age:")) 
str=input("enter the name:")
biodata(str,age =a)    
