# day 6
# 3. Write a python program using function for dice which displays
# different output after every time the user rolls the dice.
# You should ask the user whether he wishes to roll again or quit.
# (note:use the random module)

import random


def dice():
    while True:
        wishes = input("Do you want to roll the Dice(Y/y or N/n): ").lower()
        if wishes == "y" or wishes == "n":
            if wishes == "y":
                print(random.randint(1, 6))
            else:
                break
        else:
            print("Wrong input! Enter again.")
            pass


dice()