class employee:
    def __init__(self,salary,hours_of_work):
        self.salary = salary
        self.hours_of_work = hours_of_work
    def based_on_salary(self):
        if(self.salary < 5000 and self.hours_of_work < 6 ):
            self.salary = self.salary + 500
            print("your salary is",self.salary)
            print("your work is ",self.hours_of_work)
                
        elif(self.hours_of_work >= 6 and self.salary < 5000 ):
            self.salary = self.salary +750
            print("your salary is",self.salary)
            print("your work is ",self.hours_of_work)
        else:
            print(self.salary,"rs")
            print(self.hours_of_work,"hours")
            
s = int(input("enter the salary : ")) 
h = int(input("enter the hours of work per day : "))

p = employee(s,h)
p.based_on_salary()
