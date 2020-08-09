# 3) A student will not be allowed to sit in exam if his/her attendence is less than 75%.
#    Take following input from user
#    Number of classes held
#    Number of classes attended.
#    And print
#    percentage of class attended
#    Is student is allowed to sit in exam or not.

# input from user
held = int(input("Enter the total number of classes held: "))
attended = int(input("Enter the number of classes attended by student: "))

# attendance and allowed or not
percentage = (attended/held) * 100
if 75 <= percentage <= 100:
    print("Your attendance: ", percentage, "%")
    print("You are eligible for the examination!")
elif percentage > 100:
    print("Lol, Buddy! Enter the correct data atleast")
else:
    print("Your attendance: ", percentage, "%")
    print("Sorry, you cannot appear in exams this year.")