# 5. Prompt the use for an item price(using a function).
# Apply a 20% discount to the price (using a function).
# Print the starting price and the discounted price.
# Don’t accept price values less than $0.05 – repeatedly ask the user to enter new data if this happens.
# Repeat the discounting process until the user elects to stop entering data.


def item_price(price):
    print("Starting price: $", float(price))


def discounted_price(price):
    discount = price - price * 0.2
    print("Discounted price: ", discount)


print("Press 'Q/q' to exit!")
while True:
    y = input("Do you want to continue:(Y/N/Q) ").lower()
    p = float(input("Enter the price: "))
    if p > 0.05 and y == "y":
        item_price(p)
        discounted_price(p)
    elif y == "q" or y == "n":
        break
    else:
        print("Wrong input: please enter again!")
        pass

