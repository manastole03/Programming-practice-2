# Python program to display a person's info
class Person():
    def __init__(self,fname,lname,age,dob,sex,address,mob_no):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.dob = dob
        self.sex = sex
        self.address = address
        self.mob_no = mob_no

    def display(self):
        print(f"Name : {self.fname} {self.lname}")
        print(f"Age : {self.age}")
        print(f"Date Of Birth : {self.dob}")
        print(f"Gender : {self.sex}")
        print(f"Address : {self.address}")
        print(f"Mobile Number : {self.mob_no}")

class Info(Person):
    pass

p = Person("A","D",19,"22/22/2222","Male","Pune", 1212121212)
i = Info("A","D",19,"22/22/2222","Male","Pune", 1212121212)
i.display()
