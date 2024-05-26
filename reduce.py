import functools
list = [0, 33, 5, 20]
def show(a, b):
    return [a, b]
z = functools.reduce(show, list)
print(z)