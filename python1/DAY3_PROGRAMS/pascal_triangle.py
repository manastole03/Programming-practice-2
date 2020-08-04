rows = int(input("Enter the number of rows : "))
for i in range(0, rows):
    res = 1
    for j in range(1, rows-i):
        print("  ", end="")

    for k in range(0, i+1):
        print("  ", res, end="")
        res = int(res * (i - k) / (k + 1))
    print()
