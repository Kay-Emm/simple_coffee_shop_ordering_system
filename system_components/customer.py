# from order import Order
class Customer:
    # order = print_order()
    def __init__(self):
        # self.order = Order.print_order()
        # self.id = id
        self.name = input("Please enter your name: ").lower()
        self.surname = input("Please enter your surname: ").lower()
        self.email = input("Please enter your email address: ").lower()
        self.password1 =  input("Please enter your password: ")
        self.password2 = input("Please confirm your password: ")  
        # self.orders =list(order)

        # data = {
        #     "id" : 1,
        #     "name" : "kay",
        #     "surname" : "lovell",
        #     "email" : "kay.lovell@gmail.com",
        #     "password"  : "TroetelDier@01"
        # }
    def cutsomer_data(self,  name, surname, email, password1, password2):
        data_collection = True
        
        while data_collection:
            self.name = name
            self.surname = surname
            self.email =email
            self.password1 = password1
            self.password2 = password2
            data = []
            if self.password1 != self.password2:
                print("Your passwords don't match. Please")
                self.password1
                self.password2

            else:
                # for i in range(4):
                    data = data.append(self.name)
                    # data.append(self.surname)
                    # data.append(self.email)
                    # data.append(self.password1)
                    # data.append(self.password2)

                print("Your profile was successfully created.\n" /
                    "Please proceed to login.")
            data_collection = False
            pass

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

        print(Customer.cutsomer_data(self,self.name, self.surname, self.email, self.password1, self.password2))

if __name__ == "__main__":

    customer_obj = Customer()   
    customer_obj.main()