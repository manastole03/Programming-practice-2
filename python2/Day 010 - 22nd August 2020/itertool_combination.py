# 4. Take a list input of car companies from the user, store the elements in a list.
# Make all possible combinations of two (or more) among the car companies using
# "itertools.combinations" from itertools module.
# (sample data and output : list = ['hyundai', 'mahindra', 'tata', 'mg', 'renault']
# o/p: ('hyundai', 'mahindra')
# ('hyundai', 'tata')
# ('hyundai', 'mg')
# ('hyundai', 'renault')
# ('mahindra', 'tata')
# ('mahindra', 'mg')
# ('mahindra', 'renault')
# ('tata', 'mg')
# ('tata', 'renault')
# ('mg', 'renault')


import itertools

inp = list(map(str, input().split()))
print(tuple(itertools.combinations(inp, 2)))
