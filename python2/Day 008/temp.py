#   day 8
# 4. Create a Temperature class. Make two methods :
#     i. convertFahrenheit - It will take celsius and will print it into Fahrenheit.
#     ii. convertCelsius - It will take Fahrenheit and will convert it into Celsius.


class Temperature:
    def __init__(self, c, f):
        self.c = c
        self.f = f

    def convert_fahrenheit(self):
        a = (self.c * (9 / 5)) + 32
        print(f"{self.c}C is equal to {a}F.")

    def convert_celsius(self):
        b = (self.f - 32) * (5/9)
        print(f"{self.f}F is equal to {b}C.")


print("What operation you want to perform?")
print("""
1. Convert Celsius to Fahrenheit
2. Convert Fahrenheit to Celsius
Note: Press any number to exit.""")
while True:
    o = int(input("Input: "))
    if o == 1:
        p = int(input("Enter the temperature in Celsius: "))
        o1 = Temperature(p, None)
        o1.convert_fahrenheit()
    elif o == 2:
        q = int(input("Enter the temperature in Fahrenheit: "))
        o2 = Temperature(None, q)
        o2.convert_celsius()
    else:
        break



