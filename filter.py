l = [3, 6, 8, 6, 5, 6, 3, 1 ,33, 66, 43, 34]
def filt(x):
    if x < 34:
        return x
    
a = filter(filt, l)
print(list(a))