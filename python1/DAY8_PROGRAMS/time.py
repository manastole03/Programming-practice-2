# Python program to calculate time
class Time(object):
    def __init__(self,hours,minutes):
        self.hours = hours
        self.minutes = minutes

    def addTime(time1,time2):
        res_time = Time(0,0)
        res_time.hours = time1.hours+time2.hours
        res_time.minutes = time1.minutes + time2.minutes
        if res_time.minutes>=60:
            res_time.hours+=1
            res_time.minutes-=60
            return res_time

    def displayTime(self):
        print("The resultant time is {} hours and {} minutes.".format(self.hours,self.minutes))

    def displayMinutes(self):
        print("The total minutes are {}".format(self.hours*60+self.minutes))

h1 = int(input("Enter hour 1:  "))
m1 = int(input("enter minutes after hour 1:  "))
h2 = int(input("Enter hour 2:  "))
m2 = int(input("Enter minutes after hour 2:  "))

t1 = Time(h1,m1)
t2 = Time(h2,m2)
res_time = Time.addTime(t1,t2)

res_time.displayTime()
res_time.displayMinutes()
