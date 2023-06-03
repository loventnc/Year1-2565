knum = list(range(-5,5))
knumeven = list(filter(lambda a: a%2 == 0 ,knum))
print(knumeven)

knumbrook = list(filter(lambda b: b>=0 , knum))
print(knumbrook)