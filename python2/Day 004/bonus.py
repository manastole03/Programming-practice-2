# 2) A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
#    Ask user for their salary and year of service and print the net bonus amount.

print("We will be calculating the net bonus you will be getting! So please"
      " enter the correct details.")
print()
# Asking for input
salary = int(input("Enter your salary: "))
year = int(input("Enter Year of Service: "))
bonus = (salary * 0.05)

# Writing conditions
if year >= 5:
    net_bonus = salary + bonus
    print("Congratulations! You are eligible for bonus and you got"
          " a bonus of Rs.", bonus)
    print("Your Salary: ", net_bonus)
else:
    print("Sorry! You are not eligible for bonus!")
    print("Your Salary: ", salary)
