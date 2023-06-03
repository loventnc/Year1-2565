from functools import reduce
x = reduce(lambda a,b: str(a)+str(b) , list(range(10)))
print(x)