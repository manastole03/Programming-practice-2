# Python program to demonstrate whether an year is leap or not.
def leap_year(year):
    if len(year)==4:

        if int(year) % 4 == 0 and (year) % 4 == 0:
            print("The year {} is a leap year".format(year))
        else:
            print("The year {} is not a leap year".format(year))
    else:
        print("The year should be 4-digit.")
year = input("Please enter the year:  ")
leap_year(year)
