class exam:
    def __init__(self,exam_number,s1,s2,s3,s4):
        self.exam_number = exam_number
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        
    def marks(self):
        print(self.exam_number)
        lst = [self.s1,self.s2,self.s3,self.s4]
        print(lst)
        
examnumber = int(input("enter your exam number : "))        

suba = int(input("enter the marks : "))
subb = int(input("enter the marks : "))
subc = int(input("enter the marks : "))
subd = int(input("enter the marks : "))

p = exam(examnumber,suba,subb,subc,subd)

p.marks()
