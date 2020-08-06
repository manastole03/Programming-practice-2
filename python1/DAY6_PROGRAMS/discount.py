# Python program to give a discount
def price():
    a = float(input("Please tell us the price of the item in $: "))
    discount_Price = a - (a*20)/100
    print(f"The starting price is {a} and the discount price is ${discount_Price}")

    while discount_Price<0.05:
        print("Discount price below $0.05 is not acceptable.")
        price()
        break
price()
