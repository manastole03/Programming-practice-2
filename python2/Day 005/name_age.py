# day 5
# 2. Create a function that can accept two arguments name and age and print its value.

def name_age(name, age):
    print("Name: ", name)
    print(f"Age: {age}")


n = input("Enter your Name: ")
a = int(input("Enter your age: "))

name_age(n, a)
