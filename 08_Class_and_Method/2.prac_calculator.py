class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def divided(self, a, b):
        div = a / b
        x = "{:.3f}".format(div)
        return x
    def multiply(self, a, b):
        return a * b
    
cal = Calculator()

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

choice = 1

while choice != 0:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Division")
    print("4. Multiplication")

    choice = int(input("Enter the select option: "))

    if choice == 1:
        print(cal.add(a, b))
    elif choice == 2:
        print(cal.subtract(a, b))
    elif choice == 3:
        print(cal.divided(a, b))
    elif choice == 4:
        print(cal.multiply(a, b))
    elif choice == 0:
        print("Program is End!")
    else:
        print("Invalid select option! Please give me valid option ")