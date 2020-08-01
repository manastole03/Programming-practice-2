# Python program to check if the entered alphabet is a vowel or consonant.
n = input("Please enter the alphabet: ")
vowels = ('a','e','i','o','u','A','E','I','O','U')
if n in vowels:
    print(f"{n} is a vowel.")
else:
    print(f"{n} is a consonant.")
