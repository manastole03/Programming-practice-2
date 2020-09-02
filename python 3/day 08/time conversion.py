# conversion of hours or minutes and adding them using class and objects.
class time(object):
    def __init__(self,hour,minutes):
        self.hour = hour
        self.minute = minutes
    def addtime(time1,time2):
        res_time = time(0,0)
        res_time.hour = time1.hour + time2.hours
        res_time.minutes = time1.minutes + time2.minutes
        while(res_time.minutes<=60):
            res_time.hour+=1
            res_time.minutes-=60
        return res_time
    def displayTime(self):
        print("The resultant time is {} hours and {} minutes.".format(self.hours,self.minutes))

    def displayMinutes(self):
        print("The total minutes are {}".format(self.hours*60+self.minutes))

a1 = int(input("Enter hour 1:  "))
b1 = int(input("enter minutes after hour 1:  "))
a2 = int(input("Enter hour 2:  "))
b2 = int(input("Enter minutes after hour 2:  "))

t1 = Time(a1,b1)
t2 = Time(a2,b2)
res_time = Time.addTime(t1,t2)

res_time.displayTime()
res_time.displayMinutes()    
