# day 9
# 4. Write a Python class to convert an integer to a roman numeral.
class Roman:
    def __init__(self, num):
        self.num = num

    def int_to_roman(self):
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        roman_num = ""
        i = 0
        while self.num > 0:
            for _ in range(self.num // val[i]):
                roman_num += syb[i]
                self.num -= val[i]
            i += 1
        print("Roman num: ", roman_num)


n = int(input("Enter the integer:  "))
ob1 = Roman(n)
ob1.int_to_roman()
