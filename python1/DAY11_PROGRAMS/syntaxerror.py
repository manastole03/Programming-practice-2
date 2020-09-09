try:
    date = eval('datetime(2009, 12a, 31)')
except SyntaxError:
    print('error')
