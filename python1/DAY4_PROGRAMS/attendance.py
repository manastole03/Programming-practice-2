# Students attendance.
classes = int(input("Please enter the number of classes held:  "))
cls_attended = int(input("Please enter the number of classes attended:  "))
print("The student attendance is {}%".format((cls_attended/classes)*100))
if cls_attended >= classes * 0.75:
    print("The student is allowed to appear the exam.")
else:
    print("The student is NOT allowed to appear the exam.")
