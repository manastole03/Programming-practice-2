# 2.Write a Python program to check if the entered alphabet is a vowel or consonant
# (consider upper case as well as lower case)
alphabet = input("Enter an alphabet: ").casefold()
vowels = ['a', 'e', 'i', 'o', 'u']
for i in vowels:
    if alphabet in i:
        print(f"The '{alphabet}' you have entered is a vowel.")
        break
    else:
        print(f"You entered an consonant: {alphabet}")
        break
