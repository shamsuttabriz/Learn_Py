# abs() method
a = -39
print(abs(a)) # 39

# all() method
numbers = [12, 43, 23, 54, 67, 12, 54]
x = all(numbers)
print(x) # True

# float() method
x = 4
print(float(x)) # 4.0

# int() method 
x = 3.24555
print(int(x)) # 3

# len() method 
numbers = [12, 43, 23, 54, 67, 12, 54]
length = len(numbers)
print(length) # 7

# list() method
tuples = 12, 43, 23, 54, 67, 12, 54
print(list(tuples)) # [12, 43, 23, 54, 67, 12, 54]

# max() method 
max_value = max(numbers)
print(max_value) # 67

# min() method
min_value = min(tuples)
print(min_value) # 12

# reversed() method
reversed_value = reversed(numbers)
print(list(reversed_value)) # [54, 12, 67, 54, 23, 43, 12]

# sorted() method
sorted_value = sorted(numbers)
print(numbers) # [12, 43, 23, 54, 67, 12, 54]
print(sorted_value) # [12, 12, 23, 43, 54, 54, 67]
sorted_value = sorted(numbers, reverse=True)
print(sorted_value) # [67, 54, 54, 43, 23, 12, 12]

actors = [
    {'Name': 'Shakib khan', 'Age': 34},
    {'Name': 'Bappi khan', 'Age': 45},
    {'Name': 'Mosharaph Karim', 'Age': 37},
    {'Name': 'Al bakin tushar', 'Age' : 25},
    {'Name': 'Rakibul islam', 'Age': 24}
]

sorted_actors = sorted(actors, key = lambda actor:actor['Age'])
print(sorted_actors)
""" Output:
[
    {'Name': 'Rakibul islam', 'Age': 24},
    {'Name': 'Al bakin tushar', 'Age': 25},
    {'Name': 'Shakib khan', 'Age': 34},
    {'Name': 'Mosharaph Karim', 'Age': 37},
    {'Name': 'Bappi khan', 'Age': 45}
]
"""

sorted_actors = sorted(actors, key = lambda actor:actor['Age'], reverse=True)
print(sorted_actors)
"""Output:
[
    {'Name': 'Bappi khan', 'Age': 45},
    {'Name': 'Mosharaph Karim', 'Age': 37},
    {'Name': 'Shakib khan', 'Age': 34},
    {'Name': 'Al bakin tushar', 'Age': 25},
    {'Name': 'Rakibul islam', 'Age': 24}
]
"""

sorted_actors = sorted(actors, key = lambda actor:actor['Name'])
print(sorted_actors)
"""Output:
[
    {'Name': 'Al bakin tushar', 'Age': 25},
    {'Name': 'Bappi khan', 'Age': 45},
    {'Name': 'Mosharaph Karim', 'Age': 37},
    {'Name': 'Rakibul islam', 'Age': 24},
    {'Name': 'Shakib khan', 'Age': 34}]
"""


sorted_actors = sorted(actors, key = lambda actor:actor['Name'], reverse=True)
print(sorted_actors)
"""Output:
[
    {'Name': 'Shakib khan', 'Age': 34},
    {'Name': 'Rakibul islam', 'Age': 24},
    {'Name': 'Mosharaph Karim', 'Age': 37},
    {'Name': 'Bappi khan', 'Age': 45},
    {'Name': 'Al bakin tushar', 'Age': 25}
]
"""


