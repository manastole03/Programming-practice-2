# day 8
# 2. Write a python program that uses class to store the exam number and marks of four subjects. Use list
#  to store the marks of four subjects.

class Store:
    def __init__(self, sub1, sub2, sub3, sub4):
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3
        self.sub4 = sub4

    def marks_store(self):
        l = [self.sub1, self.sub2, self.sub3, self.sub4]
        print("marks stored successfully")
        print(l)


english = float(input("Input marks in english: "))
maths = float(input("Input marks in maths: "))
science = float(input("Input marks in science: "))
marathi = float(input("Input marks in marathi: "))

s1 = Store(english, maths, science, marathi)
s1.marks_store()