# 3. Write a python program using the itertools (use itertools.count) module to print the values starting from
# 20 till 60, but the number printed will have 8 added to it and so on.....
# (sample output : 20,28,36,44.......60)

import itertools

for i in itertools.count(20, 8):
    if i == 68:
        break
    else:
        print(i, end=' ')
