# day 8
# 5. Create a Time class and initialize it with hours and minutes.
# i. Make a method addTime which should take two time object and add them.
# E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
# ii. Make a method displayTime which should print the time.
# iii. Make a method DisplayMinute which should display the total minutes in the Time.
# E.g.- (1 hr 2 min) should display 62 minute.

# class Time:
#     def __init__(self, hours, minutes):
#         self.hours = hours
#         self.minutes = minutes
#
#     def add_time(time1, time2):
#         print("Addition: ", self.hours + self.)


class Time(object):

    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def add_time(time1, time2):
        time3 = Time(0, 0)  # creating new object
        time3.hours = time1.hours + time2.hours  # sum of hours
        time3.minutes = time1.minutes + time2.minutes  # sum of minutes
        while time3.minutes >= 60:
            time3.hours += 1
            time3.minutes -= 60
        return time3

    def display_time(self):
        print(f"Time is {self.hours} hours and {self.minutes} minutes")

    def display_minutes(self):
        print((self.hours * 60) + self.minutes, "minutes")


hr1 = int(input("Enter hour1: "))
m1 = int(input("Enter minute1:"))
hr2 = int(input("Enter hour2: "))
m2 = int(input("Enter minute2:"))

a = Time(hr1, m1)
b = Time(hr2, m2)
c = Time.add_time(a, b)

c.display_time()
c.display_minutes()
