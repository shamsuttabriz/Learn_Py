myPets = ['Biki', 'Harry', 'George']

print("Enter the pet name: ", end='')
name = input()
if name not in myPets:
    print('I do not have my pet name' + name)
else:
    print(name + ' is my pet')
 