from order import print_order
class Customper:
    # order = print_order()
    def __init__(self, id, name, surname, email, password, order):
        self.order = print_order()
        self.id = id
        self.name =name
        self.surname =surname
        self.email =email
        self.password =  password
        self.orders =list(order)

    def customer_order_placed(self, order):
       self.orders.append(order)
       print('{name}, Your order has been placed successfully\n'\
             'Order number: {order.id}\n'\
                'Your odered: {self.orders}')

    def view_order_history(self):
        if self.orders:
            for order in self.orders:
                if not order:
                    print(f'No order has been placed for {self.name}')
                else:
                    print(f'Here is your order history: {self.orders}')

        pass