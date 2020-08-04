def showEmployee(name,salary):
    print("Name of employee:  {}".format(name))
    print("Salary of employee:  {}".format(salary))
name = input("Please enter your name:  ")
salary = input("Enter your salary:  ")
if salary =='':
    showEmployee(name,salary = '9000')
else:
    showEmployee(name,salary)
