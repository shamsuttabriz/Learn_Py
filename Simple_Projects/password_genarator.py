import random

print("Welcome to Password Generator:")

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()0123456789"

num_of_pass = int(input("Amount of password generate: "))
len_of_pass = int(input("Enter the length of password: "))

for n in range(num_of_pass):
    password = ''
    for c in range(len_of_pass):
        password += random.choice(chars)
    print(password)

