# 5.Write Python program to check if the number is an Armstrong number or not
# (do not use the 'def' function)
# If 1³+5³+3³ = 153 ala tar it's amstrong
# Length of the number 3 ahe na, mag 3 ne cube karayacha
# Ani if sum == original no., the no. is amstrong no.

# Algorithm:
# 1 . Start
# 2 . read number
# 3 . set sum=0 and duplicate=number
# 4 . reminder=number%10
# 5 . sum=sum+(reminder*reminder*reminder)
# 6 . number=number//10
# 7 . repeat steps 4 to 6 until number > 0
# 8 . if sum = duplicate
# 9 . display number is armstrong
# 10. else
# 11. display number is not armstrong
# 12. stop

num = int(input("Enter a Number: "))
sum = 0
duplicate = num

while duplicate > 0:
    remainder = duplicate % 10

    sum = sum + (remainder ** len(str(num)))
    duplicate = duplicate//10
if sum == num:
    print("The number is armstrong!")
else:
    print("The number is not armstrong number!")
