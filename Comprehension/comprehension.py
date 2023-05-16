numbers =  [12, 43, 23, 54, 67, 45, 62, 52]

""" Normal way print odd numbers """
odd_numbers = []
for num in numbers:
    if num % 2 == 1:
        odd_numbers.append(num)
print(odd_numbers) # [43, 23, 67, 45]


""" Print even numbers with comprehension """
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers) # [12, 54, 62, 52]

some_numbers = [num for num in numbers if num % 2 == 0 if num >= 40]
print(some_numbers) # [54, 62, 52]


""" Nested for loop"""
names = ['Shakib', 'Mahmudullah', 'Mushfik']
ages = [34, 38, 35]

for name in names:
    for age in ages:
        print(name, age)

    """Output:
       -------
        Shakib 34
        Shakib 38
        Shakib 35
        Mahmudullah 34
        Mahmudullah 38
        Mahmudullah 35
        Mushfik 34
        Mushfik 38
        Mushfik 35
    """
# with comprehension method

pairs = [(name, age) for name in names for age in ages if age % 2 == 0]
print(pairs) # [('Shakib', 34), ('Shakib', 38), ('Mahmudullah', 34), ('Mahmudullah', 38), ('Mushfik', 34), ('Mushfik', 38)]


