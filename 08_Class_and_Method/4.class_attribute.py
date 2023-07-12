class Shop:
    cart = []

    def __init__(self, buyer):
        self.buyer = buyer

    def add_to_cart(self, item):
        self.cart.append(item)

shopper_1 = Shop('Alu Khan')
shopper_1.add_to_cart('T-Shirt')
print(shopper_1.cart) # ['T-Shirt']

shopper_2 = Shop('Morich Khan')
shopper_2.add_to_cart('Shoes')
print(shopper_2.cart) # ['T-Shirt', 'Shoes']
