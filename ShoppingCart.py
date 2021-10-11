class Customer:
    def __init__(self, name, balance, status):
        self.name = name
        self.balance = balance
        self.status = status

    def check_balance(self):  # how much money Customer has
        return self.balance

    def __str__(self):
        return '{self.name} has ${self.balance}'.format(self=self)


class LoyalCustomer(Customer):
    def __init__(self, name, balance, status):
        Customer.__init__(self, name, balance, status)
        self.name = name + status

    def customer_status(self):
        cus_status = self.status
        return cus_status

    def __str__(self):
        customers = (self.name + " has $" + str(self.balance) + " and is a Loyal Customer")
        return customers


class BargainHunter(Customer):
    def __init__(self, name, balance, status):
        Customer.__init__(self, name, balance, status)
        self.name = name + status

    def customer_status(self):
        cus_status = self.status
        return cus_status

    def __str__(self):
        customers = (self.name + " has $" + str(self.balance) + " and is a Bargain Hunter")
        return customers


class ShoppingCart:
    def __init__(self, ):
        self.total = 0
        self.items = dict()

    def add_item(self, name, quantity, price):      # adds item to cart
        self.items[name] = quantity
        self.total += (quantity * price)

    def remove_item(self, name, quantity, price):   # remove item from cart
        self.items[name] -= quantity
        self.total -= (quantity * price)

    def check_item(self):                           # displays dictionary with items added
        return self.items

    def check_price(self):                          # displays the added price of all items in cart
        return self.total

    def checkout(self, amount):                     # gets the difference between customer balance and price of items
        balance = amount - self.total
        return str(balance)

    def __str__(self):
        return '{self.items} cost ${self.total}'.format(self=self)


# Variables:
user1 = Customer("Blank", 0, "Blank")   # assign user to the class
cart = ShoppingCart()                   # assign cart to the class
condition1 = 0                          # conditions to prevent user from doing anything before creating a customer
condition2 = 0
item_list = {}      # Empty set to combine the two item sets later
item_list_BH = {"Rice": {"Quantity": 20, "Price": 30},  # Item list
                "Fruit": {"Quantity": 10, "Price": 10},  # (LC) = Loyal Customer only
                "Water": {"Quantity": 10, "Price": 15}}
item_list_LC = {"TV(LC)": {"Quantity": 5, "Price": 100},
                "Car(LC)": {"Quantity": 2, "Price": 200}}

# MAIN MENU:
while True:  # Main menu that will prompt the user
    user_input = input("What would you like to do?\n"  # main interface
                       "1.Create a customer\n"
                       "2.List Products\n"
                       "3.Add/remove a product to the shopping cart\n"
                       "4.See current shopping cart\n"
                       "5.Checkout\n"
                       ">")

    if user_input == '1':  # If user inputs 1   (Create customer)
        customer_name = str(input("Enter the customer's name: "))
        customer_bal = input("Enter the customer's balance: ")
        try:
            val = int(customer_bal)
        except ValueError:
            print("you must enter an integer\n")
            continue

        customer_type = input("Enter what applies to the customer:\n"  # determines if customer
                              "Loyal Customer [1]\n"  # is a Loyal Customer or
                              "Bargain Hunter [2]\n"  # Bargain Hunter
                              ">")

        if customer_type == "1":  # Customer is a Loyal Customer
            user1 = LoyalCustomer(customer_name, customer_bal, "(LC)")
            print(user1, "\n")
            condition1 = 1

        elif customer_type == "2":  # Customer is a Bargain Hunter
            user1 = BargainHunter(customer_name, customer_bal, "(BH)")
            print(user1, "\n")
            condition1 = 1

        else:
            print("invalid input\n")
            condition1 = 0

    elif user_input == "2":  # if user inputs 2     (Show item list)
        if condition1 == 1:

            if user1.customer_status() == "(LC)":               # if user is (LC) Display (BH) items and (LC) items
                item_list = {**item_list_BH, **item_list_LC}    # Combines the two item sets

            elif user1.customer_status() == "(BH)":             # if user is (BH) Display only BH items
                item_list = dict(item_list_BH)

            for product, elements in item_list.items():  # Prints out the dictionary with all the items
                print("\n---", product, "---")  # Line 66
                for info, value in elements.items():
                    print(info, ":", value, "\n")
        else:
            print("Create a customer first\n")

    elif user_input == '3':  # if user inputs 3 (Adding or removing items)
        if condition1 == 1:

            if user1.customer_status() == "(LC)":               # Checks the customer status
                item_list = {**item_list_BH, **item_list_LC}    # combines the two item sets
            elif user1.customer_status() == "(BH)":
                item_list = dict(item_list_BH)                  # Only (BH) item set

            add_or_remove = input("Do you want to add or remove a product? (a/r) ")
            if add_or_remove.lower() == "a":  # User wants to add an item to the cart
                item = input("What item do you want to add and how many? ")  # ask user for item and amount
                item_name, item_quantity = item.split()
                if item_name in item_list:  # checks if item is in item list
                    try:
                        val = int(item_quantity)
                    except ValueError:
                        print("you must enter an integer\n")
                        continue
                    if int(item_quantity) <= item_list[item_name]["Quantity"]:  # Checks if the item is in stock
                        print("added", item_quantity, item_name, "to your cart\n")
                        item_list[item_name]["Quantity"] -= int(item_quantity)  # removes the quantity from the dict
                        cart.add_item(item_name, int(item_quantity), int(item_list[item_name]['Price']))
                        condition2 = 1
                    else:
                        print("Not enough", item_name, "in stock\n")  # user requested is greater than in stock
                else:
                    print("Item not in item list\n")  # user didnt enter a valid item name

            elif add_or_remove.lower() == "r":
                item = input("What item do you want to remove and how many? ")  # ask user for item and amount
                item_name, item_quantity = item.split()
                if item_name in cart.check_item():
                    try:
                        val = int(item_quantity)
                    except ValueError:
                        print("you must enter an integer\n")
                        continue
                    print("Removed ", item_quantity, item_name, " to your cart\n")
                    item_list[item_name]["Quantity"] += int(item_quantity)  # adds the quantity back into the dict
                    cart.remove_item(str(item_name), int(item_quantity), int(item_list[item_name]['Price']))
                else:
                    print("Item not in cart\n")  # item is not in the cart
            else:
                print("Please Enter 'a' or 'r'\n")  # user input something other than 'a' or 'r'
        else:
            print("Create a customer first\n")  # user must create a customer first

    elif user_input == '4':  # if user inputs a 4  (See whats in user's cart)
        if condition1 == 1:
            print("Your cart:", cart, "\n")  # shows the user their cart and the cost of all the items
        else:
            print("Create a customer first\n")  # user must create a customer first

    elif user_input == '5':  # if user inputs a 5 (Check out)
        if condition1 & condition2 == 1:
            print("Your Balance: $" + user1.check_balance(), "\n" +  # shows the user their balance
                  "Your Bill: $" + str(cart.check_price()), "\n" +  # cost of the items
                  "Your Change: $" + cart.checkout(int(user1.check_balance())), "\n")  # balance - cost = user's change
            checkout_confirm = input("Are you happy with this transaction?(y/n)\n"
                                     ">")
            if checkout_confirm.lower() == 'y':  # user wants to checkout
                if int(cart.checkout(int(user1.check_balance()))) < 0:
                    print("Not enough money in your balance\n")
                else:
                    quit("Thank you for shopping")
            elif checkout_confirm.lower() == 'n':  # user doesn't want to checkout
                print("")
                continue
            else:
                print("invalid input\n")

        elif condition1 == 0:
            print("Create a customer first\n")  # user must create a customer first
        elif condition2 == 0:
            print("Buy an item before checking out\n")  # user must have an item in their cart before checkout

    else:  # if user inputs anything else
        print("Invalid input\n")  # error message
