Tuple1 = (99, 'cd')
Tuple2 = ('ab', 78)
print(f'From the original Tuple 1 = {Tuple1} \n\tand Tuple2 = {Tuple2} \nThe newly swapped tuples are:')
Tuple1,Tuple2 = Tuple2,Tuple1
print('Tuple 1 =', Tuple1)
print('Tuple 2 =', Tuple2)
