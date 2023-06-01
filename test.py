# class Restaurant:
#     """ 
#         menu
#         order method
#         bill generate
#         bill print
#     """
#     None

# class Menu:
#     """
#         food list
#         food add
#         food delete
#     """

# class Food:
#     """
#         food name
#         food price
#         food amount
#     """
#     None

# class Order:
#     """
#         Total Price 
#         Food list
#     """
#     None

# def main():
#     restaurant = Restaurant()
#     menu = Menu()

class revrange:
    def __init__(self, n):
        self.n = n
        self.i = n

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.n >= 0:
            if self.i == self.n:
                self.n -= 1
                return self.i
            else:
                self.i = self.n
                self.n -= 1
                return self.i
        else:
            raise StopIteration
        
for temp in revrange(0):
    print(temp)