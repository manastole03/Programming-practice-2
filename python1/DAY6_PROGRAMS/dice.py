# Python program to roll a dice.
import random
a = input("Do you want to roll the dice? (Y or N):   ")
while True:
    if a == 'Y':
        print('Dice output: ',random.randint(1,6))
    elif a =='N':
        print("Thank You.")
        break
    else:
        print("Wrong input.")
    break
while True:
    b = input("Do you want to roll again? (Y or N):  ")
    if b =='Y':
        print('Dice output: ',random.randint(1,6))
    elif b =='N':
        break
    else:
        print("Error")
