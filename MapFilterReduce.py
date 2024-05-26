import functools
# Map function implementation
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
squares = map(lambda x : x*x , numbers)
print(list(squares))

# Filter function implementation
age = [23, 18, 10, 33, 50, 15, 16]
minors = filter(lambda x : x <=18 , age)
print(list(minors))

# Reduce function 
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = functools.reduce(lambda x, y : x + y, list)
print(sum)