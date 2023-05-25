class Phone:
    manufacture = 'china'

    def __init__(self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color

    def send_sms(self, number, text):
        sms = f'sending: {text} to {number}'
        return sms
    
my_phone = Phone('Oppo', 13000, 'Blue')
print(my_phone.brand, my_phone.price, my_phone.price) # Oppo 13000 Blue
print(my_phone.manufacture) # china

her_phone = Phone('iPhone', 85000, 'Purple')
print(her_phone.brand, her_phone.price, her_phone.color) # iPhone 85000 Purple

dad_phone = Phone('Nokia', 7000, 'Black')
print(dad_phone.brand, dad_phone.price, dad_phone.color) # Nokia 7000 Black


print(my_phone.price, her_phone.price, dad_phone.price) # 13000 85000 7000