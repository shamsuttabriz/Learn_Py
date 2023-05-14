numbers = [12, 43, 23, 54, 67, 12, 54]

setNums = {12, 43, 23, 54, 67, 12, 54}

print(numbers) # [12, 43, 23, 54, 67, 12, 54]

# sets
""" set does not support duplicate values """ 
""" set does not maintain order """ 
print(setNums) # {67, 54, 23, 43, 12}

# using set method
numSetWithMethod = set(numbers)
print(numbers) # [12, 43, 23, 54, 67, 12, 54]
print(numSetWithMethod) # {67, 43, 12, 54, 23}

# add method in set
print(setNums) # {67, 54, 23, 43, 12}
setNums.add(20) # 20 is added to the set because 20 is not in the set.
print(setNums) # {67, 20, 54, 23, 43, 12}
setNums.add(67) # 67 is not added to the set because 20 is duplicate value in the set.
print(setNums) # {67, 20, 54, 23, 43, 12}

# remove method in set
setNums.remove(67)
print(setNums) # {20, 54, 23, 43, 12}