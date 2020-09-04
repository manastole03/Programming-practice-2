class employee:
    def __init__(self,salary,hours_of_work):
        self.salary = salary
        self.hours_of_work = hours_of_work
    def based_on_salary(self):
        if(self.salary < 5000):
            self.salary = self.salary + 500
            print(self.salary)
        else:
            print("no increment is there.")            
    def based_on_hours(self):
        if(self.hours_of_work >6):
            self.salary = self.salary +750
            print(self.salary)
        else:
            print("no increment is there.")
            
s = int(input("enter the salary : ")) 
h = int(input("enter the hours of work per day : "))

p = employee(s,h)
p.based_on_salary()
p.based_on_hours()
