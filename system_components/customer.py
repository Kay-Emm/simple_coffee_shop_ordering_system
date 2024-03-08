# from order import Order
import json
import os

class Customer:
    # order = print_order()
    def __init__(self):
        # self.order = Order.print_order()
        # self.id = id
        pass

    def customer_registration_info(self) -> dict:

        self.name = input("Please enter your name: ").lower()
        self.surname = input("Please enter your surname: ").lower()
        self.email = input("Please enter your email address: ").lower()
        self.password1 =  input("Please enter your password: ")
        self.password2 = input("Please confirm your password: ")  

        registration_info = {"name": self.name,
        "surname": self.surname,
        "email": self.email,
        "password1": self.password1,
        "password2": self.password2
        }
        return registration_info
        
    def cutsomer_data(self) -> dict:
        data_collection = True
        try:
            while data_collection:
                registration_info = Customer.customer_registration_info(self)
                if self.password1 != self.password2:
                    raise PasswordMismatchError("Your passwords don't match. Please repeat the registration proces.")
                else:
            
                    print("Your profile was successfully created.\n"
                        "Please proceed to login.")
                    print("data: ", registration_info)
                    data_collection = False
                return registration_info
        except PasswordMismatchError as e:
            print(f"Error: {e}")
    
    def create_database(self, data):
    #     project_folder = os.path.dirname(os.path.abspath(__file__))
    #     # file_path = os.path.join(project_folder, "data",  "customer_database.json")
    #     # print("project folder: ",project_folder)
    #     file_path = "/home/ether/Documents/github/my_repos/simple_coffee_shop_ordering_system/database/customer_database.json"
    #     with open(file_path, "a") as json_file:
    #         json.dump(data, json_file)
        file_path = "/home/ether/Documents/github/my_repos/simple_coffee_shop_ordering_system/database/customer_database.json"

               # Ensure the file exists and has valid JSON content
        if os.path.exists(file_path):
            with open(file_path, "r") as existing_file:
                try:
                    existing_data = json.load(existing_file)
                except json.JSONDecodeError:
                    existing_data = []
        else:
            # If the file doesn't exist, create it with the new data
            existing_data = []

        # Append the new data to the existing data
        existing_data.append(data)

        # Write the updated data back to the file
        with open(file_path, "w") as json_file:
            json.dump(existing_data, json_file)
            json_file.write("\n")
               # Ensure the file exists and has valid JSON content
        if os.path.exists(file_path):
            with open(file_path, "r") as existing_file:
                try:
                    existing_data = json.load(existing_file)
                except json.JSONDecodeError:
                    existing_data = []
        else:
            # If the file doesn't exist, create it with the new data
            existing_data = []

        # Append the new data to the existing data
        existing_data.append(data)

        # Write the updated data back to the file
        with open(file_path, "w") as json_file:
            json.dump(existing_data, json_file)
            json_file.write("\n")       

        def sign_up(self, name, surname,email,password1, password2):
            "Welcome to Oakridge Coffee Corner! Let's have you signed up."
            
            pass

    # def customer_order_placed(self, order):
    #    self.orders.append(order)
    #    print('{name}, Your order has been placed successfully\n'\
            #  'Order number: {order.id}\n'\
                # 'Your odered: {self.orders}')
# 
    # def view_order_history(self):
        # if self.orders:
            # for order in self.orders:
                # if not order:
                    # print(f'No order has been placed for {self.name}')
                # else:
                    # print(f'Here is your order history: {self.orders}')
# 
        # pass

    def main(self):
    #    reg_data = Customer.customer_registration_info(self)
       data = Customer.cutsomer_data(self)
       Customer.create_database(self, data)

if __name__ == "__main__":

    customer_obj = Customer()   
    customer_obj.main()