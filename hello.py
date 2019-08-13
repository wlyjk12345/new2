from functools import reduce
def fn(x,y):
    return x * 10 + y
s=reduce(fn,[1,3,4,5])
print(s)
print(fn.__name__ )