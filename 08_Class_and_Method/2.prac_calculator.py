class Calculator:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b
    def subtract(self):
        return self.a - self.b
    def divided(self):
        try:
            div = self.a / self.b
            x = "{:.3f}".format(div)
            return x
        except ZeroDivisionError:
            return 'It is impossible to divided by zero'
    def multiply(self):
        return self.a * self.b

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

cal = Calculator(a, b)

choice = 1

while choice != 0:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Division")
    print("4. Multiplication")

    choice = int(input("Enter the select option: "))

    if choice == 1:
        print(cal.add())
    elif choice == 2:
        print(cal.subtract())
    elif choice == 3:
        print(cal.divided())
    elif choice == 4:
        print(cal.multiply())
    elif choice == 0:
        print("Program is End!")
    else:
        print("Invalid select option! Please give me valid option ")