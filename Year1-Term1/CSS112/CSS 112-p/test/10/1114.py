L = [['yyyy'], ['yyyy', 'a1', 'ff', 'xx', 'yyyy', 'a2', 'ee','ff', 'xx'], ['ghhh', 'h']]
Lgreater = [k for k in [[j for j in i if  j == 'yyyy']  for i in L] if k != []]
print(Lgreater)