""" List Value Summation Using sum() function and for loop """
numbers = [12, 43, 23, 54, 67, 12, 54]
total = sum(numbers)
print("List value Summation with sum() function:", total) # 265

# Total value of number using for loop.
total = 0
for num in numbers:
    total += num
print("List value Summation: ", total) # 265



""" Set value Summation using for loop """
sets = set(numbers)
total = 0
for num in sets:
    total += num
print("Sets value Summation: ", total) # 299



""" Tuple value Summation using for loop """
tuples = tuple(numbers)
total = 0
for num in tuples:
    total += num
print("Tuples value Summation: ", total) 



""" Dictionary """
dictionaries = {"Name" : "Tabriz", "Age" : 24, "Email" : "xyz@gmail.com"}
# only key return:
print("\nOnly key return in dictionaries: ")
for info in dictionaries:
    print(info)

# only keyValue return:
print("\nOnly keyValue return in dictionaries: ")
for info in dictionaries:
    val = dictionaries[info]
    print(val)

# Key and Value both return:
print("\nBoth Key and Value of dictionaries: ")
for key, value in dictionaries.items():
    print(key, value)




""" print index and value with enumerate() function  """
list_value = [12, 43, 23, 54, 67, 12, 54]
for i, val in enumerate(list_value):
    print(i, val)



