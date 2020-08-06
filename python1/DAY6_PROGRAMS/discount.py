# Python program to give a discount
def price(a):
    discount_Price = a - (a*20)/100
    print(f"The starting price is {a} and the discount price is ${discount_Price}")

    while discount_Price<0.05:
        print("Discount price below $0.05 is not acceptable.")
        break
a = float(input("Please tell us the price of the item in $: "))
price(a)


while True:
    b = input("Do you want to add more items.(Yes or No).")
    if b =='Yes':
        a = float(input("Please tell us the price of the item in $: "))
        price(a)
    elif b =='No':
        print("Thank you!!")
        break
    else:
        print("Error! Enter 'Yes' or 'No'.")
