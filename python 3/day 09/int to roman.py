class roman:
    def int_to_roman(self,num):
        numbers = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        romans = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
        i = 12
        rnum = ''
        while(num != 0):
            if(numbers[i] <= num):
                rnum += romans[i]
                num = num - numbers[i]
            else:
                i-=1
        return rnum
n = int(input("Enter the integer:  "))
  
print(roman().int_to_roman(n))
