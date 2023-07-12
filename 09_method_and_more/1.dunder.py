class Person:
    def __init__(self, name, age, money):
        self.name = name
        self.age = age
        self.money = money
    def __add__(self, others):
        return f'Total age is: {self.age + others.age}'
    
    def __eq__(self, others):
        return self.age == others.age

    def __gt__(self, other):
        return self.age > other.age
    
    def __lt__(self, other):
        return self.age < other.age
    
alim = Person('Alim khan', 25, 5000)
dalim = Person('Dalim Khan', 43, 67000)

print(alim + dalim)
print(alim == dalim)
print(alim > dalim)
print(alim < dalim)