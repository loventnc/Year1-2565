def p11():
    namelist = ['kitty' , 'Hinton', 'Jack', 'Ted', 'Bahab', 'Cebul', 'David', 'Koller']
    # Expeced Ans -> namelengthlist = [('kitty', 5), ('Hinton', 6), ('Jack', 4), ('Ted', 3), ('Bahab', 5), ('Cebul', 5), ('David', 5), ('Koller', 6)]
    namelengthlist = [(namelist[i], len(namelist[i])) for i in range(len(namelist))]
    return namelengthlist
print(p11())