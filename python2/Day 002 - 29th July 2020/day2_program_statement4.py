# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# (for eg: entered number is 5, output=5+55+555=615)

number = int(input("Enter a number(n): "))
nn = int("%i%i" % (number, number))
nnn = int("%i%i%i" % (number, number, number))
print("The value of n + nn + nnn: ", number + nn + nnn )
