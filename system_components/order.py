from .menu import Menu

class Order:
    '''
    A class representing a customer order in a simple menu-based ordering system.

    Attributes:
        menu (dict): A dictionary containing menu items with their names and prices.
        display_menu (None): Placeholder for displaying the menu (implementation not provided).

    Methods:
        calculate_subtotal(order: list) -> float:
            Calculates the subtotal of the order based on selected items and their prices.

        calculate_tax(subtotal: float) -> float:
            Calculates the tax for a given subtotal at a fixed rate of 15%.

        summarize_order(order: list) -> tuple:
            Summarizes the order by calculating the total cost (subtotal + tax) and extracting item names.

        prompt() -> float:
            Prompts the user to enter the amount they are paying for the order.

        calculate_change(total: float, amount_to_pay: float) -> float:
            Calculates and returns the change to be given to the customer.

        amount_payable(total: float, amount_to_pay: float) -> None:
            Handles the payment process, including checking for sufficient funds and providing change.

        print_order(order: list) -> list:
            Prints the list of items in the order.

        take_order() -> list:
            Takes user input to create a list representing the customer's order.

        main() -> None:
            Orchestrates the entire order process, from taking the order to completing the payment.

    Usage Example:
        if __name__ == "__main__":
            order_obj = Order()
            order_obj.main()
    '''

    def __init__(self):
        '''
        Initializes an Order object with a menu and a placeholder for displaying the menu.
        '''
        self.menu = Menu.menu
        self.display_menu = Menu.display_menu(self)
        
        
    def calculate_subtotal(self, order) -> float:
        """ Calculates the subtotal of an order by adding up the prices of all the items in the order.

        Args:
            order: list of dicts that contain an item name and price

        Returns:
            float = The sum of the prices of the items in the order
        """
        

        subtotal_list = []
        
        try:
            print('Calculating bill subtotal...')
            for value in self.menu.values():
                if value in order:
                    subtotal_list.append(value["price"])
            subtotal = round(sum(subtotal_list),2)
            
            return subtotal
        except TypeError as e:
            print("Unable to calculate the bill's subtotal due to an internal error")

    def calculate_tax(self, subtotal) -> float:
        ''' Calculates the tax of an order by multiplying the subtotal by 15%.

        Args:
            subtotal: the price to get the tax of

        Returns:
            float - The tax required of a given subtotal, which is 15% rounded to two decimals.
        '''
        print()
        
        try:
            print('Calculating tax from subtotal...'"\n")
            tax = (subtotal *15)/100
            return round(tax, 2)
        
        except TypeError:
            print("Unable to calculate tax due to an internal error.")

    def summarize_order(self, order) -> tuple:
        """ Summarizes the order by cal calculating the total (subtotal + tax).
        Args:
            order: list of dicts that contain an item name and price

        Returns:
            tuple of names and total. The return statement should look like 
            
            return names, total

        """ 
        try:
            subtotal = self.calculate_subtotal(order)
            tax = self.calculate_tax(subtotal)

            total = round((subtotal + tax),2)
            names = [item["name"] for item in order]
        
            print("Order:" "\n",names)
            print("Total: " , f"$ {total}")

            return names, total
        except TypeError:
            print("Unable to show your oder due to an internal error.")

    def prompt(self) -> float:
        '''
        Prompts the user to enter the amount they are paying for the order.

        Returns:
            float: The amount entered by the user.
        '''

        print("\nPlease note: We only take cash!")
        user_input= input("How much are you paying? (i.e $ 5.00) ")
        
        try:
            amount_to_pay = float(user_input)
            return amount_to_pay

        except ValueError:
            print("Invalid input. Please enter a valid amount.")
        

    def calculate_change(self, total, amount_to_pay) -> float:
        '''
        Calculates and returns the change to be given to the customer.

        Args:
            total (float): The total cost of the order.
            amount_to_pay (float): The amount paid by the customer.

        Returns:
            float: The calculated change.
        '''
            
        change = round(amount_to_pay - total,2)
        print("Your change is ", f"$ {change}.")
        return change

    def amount_payable(self, total, amount_to_pay) -> None:
        '''
        Handles the payment process, including checking for sufficient funds and providing change.

        Args:
            total (float): The total cost of the order.
            amount_to_pay (float): The amount paid by the customer.

        Returns:
            None
        '''

        while True:
            try:
                amount_to_pay = float(amount_to_pay)
                if amount_to_pay > total:
                    self.calculate_change(total, amount_to_pay)
                    break

                elif amount_to_pay < total:
                    print("You have insufficient funds, please enter a valid amount.")
                    new_amount_to_pay = self.prompt()
                    self.calculate_change(total, new_amount_to_pay)
                    break

                else:
                    print("Your change is $ 0.00")
                    break

            except ValueError:
                print("Invalid input. Please enter a valid amount.")


    def print_order(self, order) -> list:
        '''
        Prints the list of items in the order.

        Args:
            order (list): List of dictionaries representing the items in the order, each containing "name" and "price".

        Returns:
            list: The input order.
        '''

        try:
            print('\nYou have ordered ' + str(len(order)) + ' items:')

            items = [item["name"] for item in order]

            print(items)
            print()
        
            return order
        except Exception:
            print("An invalid order was placed.")

    def take_order(self) -> list:
        '''
        Takes user input to create a list representing the customer's order.

        Returns:
            list: List of dictionaries representing the items in the order, each containing "name" and "price".
        '''

        order = []
        count = 1
    
        try:
            item_num = int(input("How many items would you like to order?: "))

            if item_num <= 0:
                print("0 item orders are not permitted.\n"
                    "Exiting system...") # find a way to handle this gracefully
                exit()
            
            else:
                for i in range(item_num):
                    item = input('Select menu item number ' + str(count) + ' (from 1 to 7): ')
                    count +=1
                    # try:
                    item_index = int(item_num)
                    if 1 <= item_index <= 7:
                        order.append(self.menu[int(item)])
                    
                    else:
                        print("Invalid order number. Please enter a number between 1 and 7.")
                    
                # print(order)
                return order
                
        except ValueError:
            print('''Please insert a valid number to choose the number of items to order, and to choose the desired item.\n 
                i.e.,\n
                1. enter: 1 to order one item, 2 to order two items, etc.\n
                2. enter: 1 to choose an espresso, 2 to choose coffee, etc.)\n\n
                Please try again...
                    ''')
            exit()
            
    def main(self):
        '''
        Orchestrates the entire order process, from taking the order to completing the payment.

        Returns:
            None
        '''
        try:
            order = self.take_order()
            self.print_order(order)
            total = self.summarize_order(order)
            amount_to_pay = self.prompt()
            self.amount_payable(total[1], amount_to_pay)

        except Exception:
            print("Unable to process your order. Please try again and carefully follow the prompts.")
    
if __name__ == "__main__":
    order_obj = Order()
    order_obj.main()
