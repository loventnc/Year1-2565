L = [['yyyy'], ['yyyy', 'a1', 'ff', 'xx', 'yyyy', 'a2', 'ee','ff', 'xx'], ['ghhh', 'h']]
Lgreater0 = []
for i in L:
    Lgreater1 = []
    for j  in i:
        if len(j)>3:
            Lgreater1.append(j)
    Lgreater0.append(Lgreater1)

Lgreater = [[j for j in i if len(j)>3] for i in L ]
print(Lgreater0,Lgreater)