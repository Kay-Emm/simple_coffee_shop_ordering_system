class Menu:

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

    def display_menu(self):
        print("------- Menu -------")

        for selection in self.menu:
            print(f"{selection}. {self.menu[selection]['name'] : <9} | {self.menu[selection]['price'] : >5}")

        print()
    pass