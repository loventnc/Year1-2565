tuple1 = ('ab', 78)
tuple2 = (99, 'cd') 
tuple1,tuple2 = tuple2,tuple1
print(f"From the original Tuple 1 = ('ab', 78 ) \n\tand Tuple2 = (99, 'cd')  \nThe newly swapped tuples are: ")
print(f"Tuple 1 = {tuple1}")
print(f"Tuple 2 = {tuple2}")