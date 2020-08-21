# Python class Employee.
class Employee():
    def __init__(self,salary,hours):
        self.salary = salary
        self.hours = hours

    def addsalary(self):
        if self.salary < 5000 and self.hours<6:
            self.salary += 500
            print("The final salary of the employee is Rs:  ",self.salary)
            print("The employee works for ",self.hours,"hours per day.")
        elif self.salary < 5000 and self.hours >=6:
            self.salary +=750
            print("The final salary of the employee is Rs:  ",self.salary)
            print("The emplyee works for ",self.hours,"hours per day.")
        else:
            print("The salary of the employee is Rs:  ",self.salary)
            print("The emplyee works for ",self.hours,"hours per day.")

salary = int(input("Enter the salary of employee:  "))
hours = int(input("Enter the no. of hours that the employee works per day:  "))

e = Employee(salary,hours)

e.addsalary()
