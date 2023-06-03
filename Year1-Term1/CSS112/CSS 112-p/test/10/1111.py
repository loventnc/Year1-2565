l = []
fruits = ['apple','banana','carrot']
num = list(range(3))
for i in fruits:
 for j in num: 
    l.append((i,j))
print(l)

ll = [(i,j) for i in fruits for j in num]
print(ll)