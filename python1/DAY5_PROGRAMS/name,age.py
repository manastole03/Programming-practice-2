# Python function that accepts 2 arguments name and age and print its value.
def name_age(name,age):
    print("Your name is {}".format(name))
    print("Your age is {}".format(age))
name = input("Enter your name:  ")
age = int(input("Enter your age:  "))
name_age(name,age)
