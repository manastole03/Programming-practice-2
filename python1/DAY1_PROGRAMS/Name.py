# Program which accepts the user's first and last name and print them in reverse order with a space between them.
name = input("Please enter your name: ").split()
a = name[::-1]
print(*a,sep = " ")
