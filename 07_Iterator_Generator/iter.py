"""
numbers = [12, 43, 16, 23, 83, 45, 29]
numbers_iter = iter(numbers)

print(next(numbers_iter))
print(next(numbers_iter))
print(next(numbers_iter))
print(next(numbers_iter))
print("I am exploring iterator!")
print("I am confused about it!")
print(next(numbers_iter))
print(next(numbers_iter))
print(next(numbers_iter))
print(next(numbers_iter))
print(next(numbers_iter))
print("Iteration is stopped")

"""

"""Output:
    12
    43
    16
    23
    I am exploring iterator!
    I am confused about it!
    83
    45
    29
    Traceback (most recent call last):
    File "D:\PH_Python\#anis_vai\Learn_Py\07_iterator_generator\iter.py", line 13, in <module>
        print(next(numbers_iter))
            ^^^^^^^^^^^^^^^^^^
    StopIteration
"""

numbers = [12, 43, 16, 23, 83, 45, 29]
numbers_iter = iter(numbers)
try:
    print(next(numbers_iter))
    print(next(numbers_iter))
    print(next(numbers_iter))
    print(next(numbers_iter))
    print("I am exploring iterator!")
    print("I am confused about it!")
    print(next(numbers_iter))
    print(next(numbers_iter))
    print(next(numbers_iter))
    print(next(numbers_iter))
    print(next(numbers_iter))
except StopIteration:
    print("Iteration is stopped")   

"""Output:
    12
    43
    16
    23
    I am exploring iterator!
    I am confused about it!
    83
    45
    29
    Iteration is stopped
"""