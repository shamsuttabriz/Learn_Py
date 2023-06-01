class Shopper:

    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, item, price, quantity):
        self.cart.append({'item': item, 'price': price, 'quantity': quantity})

    def checkout(self, amount):
        price = 0
        for item in self.cart:
            print(item)
            price = price + item['price'] * item['quantity']
        print(f'Total Price: {price}') # Total Price: 12858
        if amount < price:
            return f'Please give me more money: {price - amount}'
        elif amount > price:
            return f'Here are the items! Extra amount: {amount - price}'
        else:
            return f'Here are the items!! No give & No back'
        

my_shop = Shopper('Akbar Ali')
my_shop.add_to_cart('Shirt', 1499, 2)
my_shop.add_to_cart('Pant', 2290, 3)
my_shop.add_to_cart('Shoes', 2990, 1)

lagbo_naki_dibo = my_shop.checkout(10000) 
print(lagbo_naki_dibo) # Please give me more money: 2858

lagbo_naki_dibo = my_shop.checkout(13000)
print(lagbo_naki_dibo) # Here are the items! Extra amount: 142

lagbo_naki_dibo = my_shop.checkout(12858)
print(lagbo_naki_dibo) # Here are the items!! No give & No back
    