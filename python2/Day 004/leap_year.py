# 1) Write a program to check if a year is leap year or not.
# If a year is divisible by 4 then it is leap year but if the year is century
# year like 2000, 1900, 2100 then it must be divisible by 400.
# ===================================================================

# Taking only 4 digit input!
while True:
    try:
        year = int(input("Enter the year to check: "))
        if 1000 < year < 10000:
            break
    except:
        pass

# checking and printing for leap year!

if year % 4 == 0:
    print(year, " is a leap year!")
elif year % 400 == 0:
    print(year, " is a leap year!")
else:
    print(year, "is not a leap year!")

# ====================================================================
# new concept learned:
#
# The "try" block lets you test a block of code for errors.
# The "except" block lets you handle the error.
# The "finally" block lets you execute code, regardless of the result of the try- and except blocks.
#
# Syntax:
#
# try:
#   print(x)
# except:
#   print("An exception occurred")
