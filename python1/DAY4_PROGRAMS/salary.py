# Program to calculate the bonus of an empolyee.
salary = int(input("Please enter your salary: "))
years = eval(input("Please enter your years of service:  "))
if years > 5:
    print("Congratulations!! Your salary has been incremented by Rs.{}".format(salary*5/100))
    print("Your salary will be Rs.{}".format(salary+salary*5/100))
else:
    print("Sorry. You didn't get any hike in your salary.")
