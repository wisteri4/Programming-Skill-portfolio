#Display the vending machine items and their prices to the user
print("""
 ===== Vending Machine =====
 
    1 - Lays Chips : 4 AED
    2 - Cheetos : 3.50 AED
    3 - Cheese Croissant: 2.50 AED
    4 - Kitkat : 4 AED
    5 - Oreo : 5 AED
    6 - Galaxy Chocolate : 3.25 AED
    7 - Green Tea : 6 AED
    8 - Coca-cola : 4 AED
    9 - Sprite : 4 AED
    10 - Water : 3 AED

""")

#Dictionary and key to hold product information: [Product Name, Price]
choose = {
    1: ["Lays Chips", 4],
    2: ["Cheetos", 3.50],
    3: ["Cheese Croissant", 2.50],
    4: ["Kitkat", 4],
    5: ["Oreo", 5],
    6: ["Galaxy Chocolate", 3.25],
    7: ["Green Tea", 6],
    8: ["Coca-cola", 4],
    9: ["Sprite", 4],
    10: ["Water", 3]
}

#Initialize stock for each product (3 items for each product)
product_stock = {key: 3 for key in choose}

#Function for vending machine operations
def vending_machine():
    cart = []  #To store chosen items for the receipt

    #Function to display the receipt and calculate the total cost
    def display_receipt(cart):
        print("\n===== Izabel's Vending Machine =====")
        total_cost = 0  #Variable to keep track of the total cost
        for item, quantity, price in cart:
            #Print each item in the cart with quantity and cost
            print(f"{item} x{quantity} - {price * quantity} AED")
            total_cost += price * quantity
        print(f"Total: {total_cost} AED")
        print("====================")
        return total_cost  #Return the total cost for payment processing

    #Main item selection loop
    while True:
        try:
            #Prompt user to enter a product code or 0 to finish selection
            prod = int(input("Enter your code or press 0 to finish selection: "))
            if prod == 0:
                break  #Exit loop if the user is done selecting items
            if prod not in choose: #If  code is not in the dictionary
                print("Invalid code. Please enter a valid product code.")
                continue  #Continue to the next iteration if the code is invalid

            available_stock = product_stock[prod] #Get the available stock for the selected product
            if available_stock == 0:
                print(f"Sorry, {choose[prod][0]} is out of stock.")
                continue  #Skip to the next iteration if the product is out of stock

            #Display available stock and prompt the user for the quantity
            print(f"There are {available_stock} {choose[prod][0]} left.")
            while True:
                try:
                    #Prompt user to specify the quantity they want
                    quantity = int(input(f"How many {choose[prod][0]}: "))
                    if quantity <= 0:
                        print("Please enter a quantity greater than 0.")
                    elif quantity > available_stock:
                        print(f"Insufficient stock. You can only purchase up to {available_stock}.")
                    else:
                        #Deduct the selected quantity from the stock
                        product_stock[prod] -= quantity
                        #Add selected product to the cart in order of item, quantity, price
                        cart.append((choose[prod][0], quantity, choose[prod][1]))
                        print(f"{quantity} {choose[prod][0]} added to your cart.")
                        break  #Exit the quantity input loop
                except ValueError: #If user inputs a symbol or string return with a message 
                    print("Invalid input. Please enter a number.")  #Handle invalid input for quantity

        except ValueError: 
            print("Invalid input. Please enter a number.")  #Handle invalid input for product code

    #If the cart is not empty then proceed to payment
    if cart:
        total_cost = display_receipt(cart)  #Display receipt and get total cost

        while True:
            try:
                #Prompt user to insert payment
                payment = float(input(f"Your total is {total_cost} AED. Please insert the total amount or more: "))
                if payment < total_cost:
                    print(f"Insufficient amount. Please insert at least {total_cost} AED.")
                else:
                    #Calculate and display change if payment is sufficient
                    change = payment - total_cost
                    if change > 0:
                        print(f"Your change is {change} AED.")
                    print("Thank you for your purchase! Please collect your items below.\n")
                    break  #Exit the payment loop
            except ValueError:
                print("Invalid input. Please enter a valid amount.")  #Handle invalid input for payment
    else:
        print("No items were purchased. Thank you!")  #Else display if no items were selected

#Main program loop to allow multiple shopping sessions
while True:
    vending_machine() #Call the vending machine function if user continues to purchase
    another_purchase= input("Enter any key to quit or c to continue to purchase: ").lower()
    if another_purchase != 'c':
        #Exit and break the loop if the user does not want another purchase 
        print("Thank you for using the vending machine! Goodbye!")
        break
