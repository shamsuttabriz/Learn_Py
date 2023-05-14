first_way_tuples = 12, 43, 23, 54, 67, 12, 54
print(first_way_tuples) # (12, 43, 23, 54, 67, 12, 54)

second_way_tuples = (12, 43, 23, 54, 67, 12, 54)
print(second_way_tuples) # (12, 43, 23, 54, 67, 12, 54)

nums = [12, 43, 23, 54, 67, 12, 54]
third_way_tuples = tuple(nums)
print(third_way_tuples) # (12, 43, 23, 54, 67, 12, 54)

# tuple may be nested
nested_tuple = first_way_tuples, (10, 34, 21, 5)
print(nested_tuple) # ((12, 43, 23, 54, 67, 12, 54), (10, 34, 21, 5))

# tuples are immutable that means tuples value are not changeable
"""
    second_way_tuples[2] = 100
    -> thats are wrong because tuple values are not changeable
"""

# tuples can contain mutable objects and that values are changeable

mutable_tuples = (['hello', 10, 78], [48, 'good', 'boy'])
print(mutable_tuples) # (['hello', 10, 78], [48, 'good', 'boy'])

mutable_tuples[0][2] = 'Harry'
print(mutable_tuples) # (['hello', 10, 'Harry'], [48, 'good', 'boy'])

