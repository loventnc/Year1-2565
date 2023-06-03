#ข้อ1.1
def p11():
    namelist = ['kitty' , 'Hinton', 'Jack', 'Ted', 'Bahab', 'Cebul', 'David', 'Koller']
    # Expeced Ans -> namelengthlist = [('kitty', 5), ('Hinton', 6), ('Jack', 4), ('Ted', 3), ('Bahab', 5), ('Cebul', 5), ('David', 5), ('Koller', 6)]
    namelengthlist = [(namelist[i], len(namelist[i])) for i in range(len(namelist))]
    return namelengthlist
print(p11())

#ข้อ1.2
def p12():
  Dr_set = {'Jeffy', 'David', 'Ted'} 
  namelist = ['kitty' , 'Hinton', 'Jack', 'Ted', 'Bahab', 'Cebul', 'David', 'Koller']
  titlednamelist =  ["Dr."+x if x in Dr_set else x for x in namelist]
  #Expected Ans -> titlednamelist = ['kitty', 'Hinton', 'Jack', 'Dr. Ted', 'Bahab', 'Cebul', 'Dr. David', 'Koller']
  return titlednamelist
print(p12())

#ข้อ1.3
def p13():
    student_names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    scores = [9, 22, 60, 58, 70, 12, 33, 99, 57, 82]
    grade_a_student_with_score = [(student_names[i], scores[i]) for i in range(len(student_names)) if scores[i] >= 80]
    #Expected Ans -> grade_a_student_with_score = [('h', 99), ('j', 82)]
    return grade_a_student_with_score
print(p13())

#ข้อ1.4
def p14():
    ddict = {'Amanda': 'Doctor', 
             'knew': 'now', 
             'how': 'in', 
             'joyous': 'great', 
             'could': 'threatening', 
             'be': 'danger,',
             'until': 'please', 
             'saw': 'need', 
             'face': 'help', 
             'leaps': 'beats', 
             'hummingbird': 'machine ', 
             'in': 'very', 
             'flight': 'alarmingly', 
             'time': 'hour,', 
             'see': 'need', 
             'you': 'the drug', 
             'inspires': 'causes', 
             "haven't": 'am'}

    
    letter="Dear Amanda I haven't knew how joyous life could be until I saw your face My heart leaps like a hummingbird in flight every time I see your face This is something I have never felt before and it is you that inspires it"
    list_letter = letter.split(" ")
    decoded_list = [ddict.get(key, key) for key in list_letter ]
    decoded_letter = ' '.join(decoded_list)
    # Expected ans-> decoded_letter = 'Dear Doctor I am now in great life threatening danger, please I need your help My heart beats like a machine  very alarmingly every hour, I need your help This is something I have never felt before and it is the drug that causes it'
    return decoded_letter
print(p14())

#ข้อ2
def p2():

    icecream_msg = 'I like to buy ice cream: choco or may be cone otherwise sherbet'
    icecream_price = {'cone':'300', 'sherbet':'200', 'choco': '100'}
    #ExpectedAns = 'I like to buy ice cream: choco for 100 or may be cone for 300 otherwise sherbet for 200'

    decoded_icecream_list = [icecream_price.get(key, key) for key in icecream_msg.split()]
    Ans = ' '.join(decoded_icecream_list)
    return Ans
print(p2())

#ข้อ3:
def p3(a,b):
  num = int(input("Enter the first value: "))
  num1 = int(input("Enter the second value: "))
  import math
  ansgcd = math.gcd(num,num1)
  print(ansgcd)
  return 0
print(p3(0,0))

#ข้อ4:
from functools import reduce

def p4():
  list_x = [1.5,2,0.5,4,5]
  fx = lambda x1,x2: (x2-x1)/(x2+x1)
  no4_ans = reduce(lambda x1,x2: fx(x1,x2), list_x)
  
  return 0
print(p4())