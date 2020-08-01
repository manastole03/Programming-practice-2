n=int(input("Number of classes held: "))
m=int(input("Number of classes attened: "))
print("Number of classes held",n)
print("Number of classes attened",m)

pcg=(m%n)*100

if(pcg>75 or pcg==75):
    print("allowed to sit in exam")
else:
    print("not allowed to sit in exam")
