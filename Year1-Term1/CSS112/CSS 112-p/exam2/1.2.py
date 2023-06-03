def p12():
  Dr_set = {'Jeffy', 'David', 'Ted'} 
  namelist = ['kitty' , 'Hinton', 'Jack', 'Ted', 'Bahab', 'Cebul', 'David', 'Koller']
  titlednamelist =  ["Dr."+x if x in Dr_set else x for x in namelist]
  #Expected Ans -> titlednamelist = ['kitty', 'Hinton', 'Jack', 'Dr. Ted', 'Bahab', 'Cebul', 'Dr. David', 'Koller']
  return titlednamelist
print(p12())