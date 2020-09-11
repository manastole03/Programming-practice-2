# Python program to get all possible unique subsets

from itertools import permutations
inp = set(map(int, input("Enter distinct integers:  ").split()))
perm = permutations(inp)
for i in perm:
    print(i)
