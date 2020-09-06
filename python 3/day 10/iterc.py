import itertools
int = list(map(str, input().split()))
print(tuple(itertools.combinations(int,2)))
