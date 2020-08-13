# Python program to store exam number and marks of four subjects.
class FourSubjects:
    def __init__(self,exam_no,s1,s2,s3,s4):
        self.exam_no = exam_no
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4

    def marks(self):
        print(self.exam_no)
        lst = [self.s1,self.s2,self.s3,self.s4]
        print(lst)

exam_number = int(input("Enter the exam number:  "))
FDS = int(input("Enter the marks in FDS:  "))
OOP = int(input("Enter the marks in OOP:  "))
DELD = int(input("Enter the marks in DELS:  "))
CG = int(input("Enter the marks in CG:  "))

a = FourSubjects(exam_number,FDS,OOP,DELD,CG)


a.marks()
