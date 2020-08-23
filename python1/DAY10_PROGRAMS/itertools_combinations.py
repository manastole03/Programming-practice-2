# Python itertools.combinations
import itertools
inp = list(map(str, input().split()))
print(tuple(itertools.combinations(inp,2)))
