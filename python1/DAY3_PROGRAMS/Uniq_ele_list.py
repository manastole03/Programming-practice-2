# Python function that takes a list and returns a new list with unique elementsof the first list.
user_input = input("Please enter the elements seperated by space: ").split()
input_list = list(map(int, user_input))
a = set(input_list)
uniq_list = list(a)
print(uniq_list)
