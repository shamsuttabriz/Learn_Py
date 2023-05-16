"""
    All method 
    lambda(), map(), filter()
"""

def double(x):
    return x * 2

print(double(4)) # 8

# same work with lambda() function
doubled = lambda num : num * 2
print(doubled(9)) # 18

# summation with 2 value
sum_value = lambda a, b : a + b
print(sum_value(5, 2)) # 7

# list value square with lambda and map method 
numbers = [12, 43, 23, 54, 67, 12, 54]

square_value  = lambda x : x * x

square_numbers = map(square_value, numbers)
print(list(square_numbers)) # [144, 1849, 529, 2916, 4489, 144, 2916]

doubled_numbers = map(lambda x : x * 2, numbers)
print(list(doubled_numbers)) # [24, 86, 46, 108, 134, 24, 108]


# filter method 
list_value = [1, 2, 3, 4, 5, 6 , 7, 8, 9, 10]
bigger_numbers = filter(lambda num: num > 5, list_value)
print(list(bigger_numbers)) # [6, 7, 8, 9, 10]

even_numbers = filter(lambda x : x % 2 == 0, list_value)
print(list(even_numbers)) # [2, 4, 6, 8, 10] 

actors = [{"Name" : "Abir", "Age" : 24},
           {"Name" : "Seam", "Age" : 34},
           {"Name" : "Rakib", "Age" : 23},
           {"Name" : "Tushar", "Age" : 55}
           ]
old_friend = filter(lambda friend : friend['Age'] <= 30, actors)
print(list(old_friend)) # [{'Name': 'Abir', 'Age': 24}, {'Name': 'Rakib', 'Age': 23}]

new_friend = filter(lambda friend : friend['Age'] >= 30, actors)
print(list(new_friend)) # [{'Name': 'Seam', 'Age': 34}, {'Name': 'Tushar', 'Age': 55}]


