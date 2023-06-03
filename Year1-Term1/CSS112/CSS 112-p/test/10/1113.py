L = [['yyyy'], ['yyyy', 'a1', 'ff', 'xx', 'yyyy', 'a2', 'ee','ff', 'xx'], ['ghhh', 'h']]

def Lgreater(L):
    if isinstance(L,str):
        if len(L)>3:
            return L
    else:
        return [[j for j in i if len(j)>3] for i in L ]

print(Lgreater(L))