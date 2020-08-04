# Rules for place of service.
age = int(input("Please enter your age:  "))
sex = input("Please enter your sex (M or F):  ")
if sex == 'F':
    print("The employee will work in urban areas only.")
elif sex == 'M' and 20<=age<=40:
    print("The employee may work anywhere.")
elif sex == 'M' and 40<=age<=60:
    print("The employee will work in urban areas only.")
else:
    print("ERROR!")
