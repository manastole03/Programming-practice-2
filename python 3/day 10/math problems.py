import math
n = int(input("enter a number : "))
p = n**(0.5)
q = 1
for i in range(1,n+1):
    q = q*i
print("factorial  ",q)    
print("square root  ",p)
print("Degrees   ", math.degrees(num))
print("Radians   ", math.radians(num))
print("Sin   ", math.sin(num))
print("Cosine   ", math.cos(num))
print("Tangent   ", math.tan(num))
print("Gamma function  ", math.gamma(num))
print("Logarithmic function   ", math.log(num,10))
