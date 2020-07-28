# Program to swap two numbers.
# using a temporary variable.
x = 1
y = 7

a = x
x = y
y = a

print("The value of x after swaping : {}".format(x))
print("The value of y after swaping : {}".format(y))

# Without using a temporary variable.
x = 1
y = 7

x = x + y
y = x - y
x = x - y
print("The value of x after swapping : {}".format(x))
print("The value of y after swapping : {}".format(y))
