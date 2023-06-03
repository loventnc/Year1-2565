def p3(a,b):
  num = int(input("Enter the first value: "))
  num1 = int(input("Enter the second value: "))
  import math
  ansgcd = math.gcd(num,num1)
  print(ansgcd)
  return 0
print(p3(0,0))