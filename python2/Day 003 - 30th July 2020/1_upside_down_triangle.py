# 1. Create an upside down star pyramid using loops.
#   ******
#   *****
#   ****
#   ***
#   **
#   *

# ---------------------------------------------

rows = int(input("Enter the number of rows: "))
for i in range(0, rows):
    for j in range(0, rows - i):
        print("*", end="")
    print()