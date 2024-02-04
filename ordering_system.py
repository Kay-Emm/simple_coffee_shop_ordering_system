menu = {
    1: {"name": 'espresso',
        "price": 1.99},
    2: {"name": 'coffee', 
        "price": 2.50},
    3: {"name": 'cupaccino',
        "price": 3.00},
    4: {"name": 'cake', 
        "price": 2.79},
    5: {"name": 'soup', 
        "price": 4.50},
    6: {"name": 'muffin',
        "price": 2.65},
    7: {"name": 'sandwich',
        "price": 4.99}
}

def calculate_subtotal(order):
    """ Calculates the subtotal of an order

    [IMPLEMENT ME] 
        1. Add up the prices of all the items in the order and return the sum

    Args:
        order: list of dicts that contain an item name and price

    Returns:
        float = The sum of the prices of the items in the order
    """
    

    subtotal_list = []
    
    try:
        print('Calculating bill subtotal...')
        for value in menu.values():
            if value in order:
                subtotal_list.append(value["price"])
        subtotal = round(sum(subtotal_list),2)
        
        return subtotal
    except TypeError as e:
        print("Unable to calculate the bill's subtotal due to an internal error")

def calculate_tax(subtotal):
    """ Calculates the tax of an order

    [IMPLEMENT ME] 
        1. Multiply the subtotal by 15% and return the product rounded to two decimals.

    Args:
        subtotal: the price to get the tax of

    Returns:
        float - The tax required of a given subtotal, which is 15% rounded to two decimals.
    """
    print()
    
    try:
        print('Calculating tax from subtotal...'"\n")
        tax = (subtotal *15)/100
        return round(tax, 2)
    
    except TypeError:
        print("Unable to calculate tax due to an internal error.")

def summarize_order(order):
    """ Summarizes the order

    [IMPLEMENT ME]
        1. Calculate the total (subtotal + tax) and store it in a variable named total (rounded to two decimals)
        2. Store only the names of all the items in the order in a list called names
        3. Return names and total.

    Args:
        order: list of dicts that contain an item name and price

    Returns:
        tuple of names and total. The return statement should look like 
        
        return names, total

    """ 
    try:
        subtotal = calculate_subtotal(order)
        tax = calculate_tax(subtotal)

        total = round((subtotal + tax),2)
        names = [item["name"] for item in order]
    
        print("Order:" "\n",names)
        print("Total: " , f"$ {total}")

        return names, total
    except TypeError:
        print("Unable to show your oder due to an internal error.")

def prompt():
    print("\nPlease note: We only take cash!")
    user_input= input("How much are you paying? (i.e $ 5.00) ")
    
    try:
        amount_to_pay = float(user_input)
        return amount_to_pay

    except ValueError:
        print("Invalid input. Please enter a valid amount.")
    

def calculate_change(total, amount_to_pay):
        
        change = round(amount_to_pay - total,2)
        print("Your change is ", f"$ {change}.")
        return change

def amount_payable(total, amount_to_pay):
    while True:
        try:
            amount_to_pay = float(amount_to_pay)
            if amount_to_pay > total:
                calculate_change(total, amount_to_pay)
                break

            elif amount_to_pay < total:
                print("You have insufficient funds, please enter a valid amount.")
                new_amount_to_pay = prompt()
                calculate_change(total, new_amount_to_pay)
                break

            else:
                print("Your change is $ 0.00")
                break

        except ValueError:
            print("Invalid input. Please enter a valid amount.")


def print_order(order):
    try:
        print('\nYou have ordered ' + str(len(order)) + ' items:')

        items = [item["name"] for item in order]

        print(items)
        print()
    
        return order
    except Exception:
        print("an invalid order was placed.")

    
# This function is provided for you, and will display the menu
def display_menu():
    print("------- Menu -------")

    for selection in menu:
        print(f"{selection}. {menu[selection]['name'] : <9} | {menu[selection]['price'] : >5}")

    print()

# This function is provided for you, and will create an order by prompting the user to select menu items
def take_order():
    display_menu()
    order = []
    count = 1
    try:
        item_num = int(input("How many items would you like to order? "))

        for i in range(item_num):
            item = input('Select menu item number ' + str(count) + ' (from 1 to 7): ')
            count += 1
            order.append(menu[int(item)])
        print()

        return order
    
    except ValueError:
        print(
            '''
            Please insert a valid number to choose the number of items to order,\n
            and to choose the desired item.\n 
            i.e.,\n
            1. enter: 1 to order one item, 2 to order two items, etc.\n
            2. enter: 1 to choose an espresso, 2 to choose coffee, etc.)
            '''
              )



def main():
    try:
        order = take_order()
        print_order(order)
        total = summarize_order(order)
        amount_to_pay = prompt()
        amount_payable(total[1], amount_to_pay)
    except Exception:
        print("Unable to process your order. Please try again and carefully follow the prompts.")
 
if __name__ == "__main__":
    main()