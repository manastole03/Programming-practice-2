#Python Store Class
class Store():
    def __init__(self, record_of_products):
        self.record_of_products = record_of_products
    
    def add_products(self):
        inp2 = input("""Here is the list of products with their respective prices.
Please enter your choice(1,2 or 3):
    1. Milk 20
    2. Biscuits 10
    3. Tea Powder 10
    """)
        while True:

            if inp2 == '1':
                record_of_products['Milk'] +=20
                print("Milk added successfully.")
                break
            elif inp2 == '2':
                record_of_products['Biscuits'] +=10
                print("Biscuits added successfully.")
                break
            elif inp2 == '3':
                record_of_products['Tea Powder'] +=10
                print("Tea Powder added successfully.")
                break
            else:
                print("Please enter a valid choice")
    
    def generate_bill(self):
        for i in record_of_products:
            print(i , record_of_products[i])
        print("The total payable price is : Rs ", (record_of_products['Milk'] + record_of_products['Biscuits'] + record_of_products['Tea Powder']))
    
    
record_of_products = {'Milk' : 0, 'Biscuits': 0, 'Tea Powder': 0}    
customer = Store(record_of_products)

def main():
    while True:
        inp1 = input("""Please enter your choice: 
        1. Purchase
        2. Generate Bill
        3. Exit
        """)
        while True:
            if inp1 == '1':
                customer.add_products()
               
                while True:
                    inp3 = input("Do you wish to shop again? (y/n):  ")
                    if inp3 == 'y':
                        customer.add_products()
                    elif inp3 =='n':
                        main()
                        break
                    else:
                        print("Enter a valid choice: ")
                break
            elif inp1 == '2':
                customer.generate_bill()
                print("Thank You for shopping at Deshpande's Store.")
                break
            elif inp1 == '3':
                print("Thank You for shopping at Deshpande's Store.") 
                break
                
        
            else:
                print("Enter a valid choice ")
        break
        
           
                
            
print("Welcome to Deshpande's Store!")

main()
