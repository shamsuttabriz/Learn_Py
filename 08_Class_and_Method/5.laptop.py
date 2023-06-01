class Laptop:
    
    def __init__(self, brand, age):
        self.brand = brand
        self.age = age

    def increase(self, age = 1):
        self.age = self.age + age

    def repair(self, after_repair = -2):
        self.increase(after_repair)

my_laptop = Laptop('Dell', 4)
my_laptop.increase()
print("Before repair age:", my_laptop.age) # Before repair age: 5
my_laptop.repair()
print("After repair age:", my_laptop.age) # After repair age: 3

