numbers = [12, 43, 16, 23, 83, 45, 29]

def get_numbers(nums):
    yield nums

result = get_numbers(numbers)
print(list(result)) # [[12, 43, 16, 23, 83, 45, 29]]

def get_numbers(nums):
    for num in nums:
        yield num
result = get_numbers(numbers)
try:
    print(next(result))
    print(next(result))
    print(next(result))
    print(next(result))
    print("I am exploring generator!")
    print("I don't know generator!")
    print(next(result))
    print(next(result))
    print(next(result))
    print(next(result))
except StopIteration:
    print("Stop the iteration")

"""Output:
    12
    43
    16
    23
    I am exploring generator!
    I don't know generator!
    83
    45
    29
    Stop the iteration
"""

