# day 5
# 3. Create a function showEmployee() in such a way that it should accept employee name,
# and it’s salary and display both,
# and if the salary is missing in function call it should show it as 9000

def show_employee(name, salary):
    print(f"Name: {name}")
    if salary == '':
        print("Salary: 9000")
    else:
        print(f"Salary: {salary}")


n = input("Enter your name: ")
s = input("Enter your salary (press enter for default value): ")
show_employee(n, s)
