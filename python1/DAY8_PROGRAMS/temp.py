# Python class to convert farenheit to celsius and vice versa
class Temperature:
    def __init__(self,celsius,farenheit):
        self.celsius = celsius
        self.farenheit = farenheit

    def convertFarenheit(self):
        print("Equivalent temperature on Farenheit scale:  ",(5/9)*(self.celsius-32))

    def convertCelsius(self):
        print("Equivalent temperature on Celsius scale:  ",(9/5)*self.farenheit+32)

celsius = float(input("Enter the temperature in degree Celsius:  "))
farenheit = float(input("Enter the temperature in degree Farenheit:  "))

t1 = Temperature(celsius,farenheit)
t2 = Temperature(celsius,farenheit)

t1.convertFarenheit()
t2.convertCelsius()
