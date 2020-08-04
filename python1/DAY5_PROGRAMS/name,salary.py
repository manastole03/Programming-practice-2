def showEmployee(name,salary=9000):
    print("Name of employee:  {}".format(name))
    print("Salary of employee:  {}".format(salary))

name = input("Enter your name:  ")
salary = int(input("Enter salary:  "))
showEmployee(name,salary)
