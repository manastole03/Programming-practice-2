#
# 5) Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and
#    then using following rules print their place of service.
#    if employee is female, then she will work only in urban areas.
#
#    if employee is a male and age is in between 20 to 40 then he may work in anywhere
#
#    if employee is male and age is in between 40 t0 60 then he will work in urban areas only.
#
#    And any other input of age should print "ERROR".

# taking input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
while True:
    try:
        sex = input("Enter your sex( M or F) : ").lower()
        married = input("Are you married? ( Y or N): ").lower()
        if (sex == 'm' or sex == 'f') and (married == "y" or married == 'n'):
            break
    except:
        pass

# conditions
if 20 <= age <= 60:
    if sex == "m":
        if 20 <= age < 40:
            print(f"Hello {name}, You can work anywhere.")
        elif 40 <= age <= 60:
            print(f"Hello {name}, You can work in Urban Area only.")
    else:
        print(f"Hello {name}, You should work in Urban Area only.")
else:
    print("You can't work!")
