# day 9
# 3. Write a program by creating an 'Employee' class having the following methods and print the final salary.
# i - Get information of the salary, number of hours of work per day of employee as parameter
# ii - Add rs500 to salary of the employee if it is less than rs5000.
# iii - Add rs750 to salary of employee if the number of hours of work per day is more than 6 hours.

class Employee:
    def __init__(self, s, h):
        self.s = s
        self.h = h

    def ii(self):
        if self.s < 5000:
            print("Salary: {0}".format(self.s + 500))
            print(f"Number of hours per day: {self.h}")
        else:
            print("Salary: {0}".format(self.s))
            print(f"Number of hours per day: {self.h}")

    def iii(self):
        if self.h > 6:
            print("Salary: {0}".format(self.s + 750))
            print(f"Number of hours per day: {self.h}")
        else:
            print("Salary: {0}".format(self.s))
            print(f"Number of hours per day: {self.h}")


salary = int(input("Enter your salary: "))
hour = int(input("Enter the number of hours per day: "))

ans = Employee(salary, hour)
print("++++++++++ Answer ii: ++++++++++++++++++++++++")
ans.ii()
print("++++++++++ Answer iii: ++++++++++++++++++++++++")
ans.iii()