#1
print('Cutie, Cutie, little girl,\n \tHow I wonder what you are!\n \t\tUp above the world so hight,\n \t\tLike a star in the sky.\n Cutie, cutie, little girl,\n \tHow I wonder what you are! ')

#2
Jacklist = ['Jack',':','How', 'are', 'you', 'today', '?']
Jimlist = ['Jim',':', "I'am", 'well', 'Thank', 'you', 'and', 'you', '?']
print(" ".join(Jacklist))
print(" ".join(Jimlist))

#3
import math
Num1 = math.sqrt(3)
ans1 = "{:.3f}".format(Num1)
Num2 = 8**(1/3)
ans2 = "{:.3f}".format(Num2)
print("The square root of 3.000 is "+str(ans1))
print("The triple root of 8.000 is "+str(ans2))

#4
C = 100
F = (9*C/5)+32
print('Temperature in',C,' Celsius =' ,F,'Fahrenheit')

#5
tuple = ("Orange", (10,20,30),(5,15,25))
print(tuple[1][1])
print(tuple[2][2])

#6
Tuple1 = (99, 'cd')
Tuple2 = ('ab', 78)
print(f'From the original Tuple 1 = {Tuple1} \n\tand Tuple2 = {Tuple2} \nThe newly swapped tuples are:')
Tuple1,Tuple2 = Tuple2,Tuple1
print('Tuple 1 =', Tuple1)
print('Tuple 2 =', Tuple2)


#7
sample_dict = {
'emp1': {'name': 'Jhon', 'salary': 7500},
'emp2': {'name': 'Emma', 'salary': 8000},
'emp3': {'name': 'Brad', 'salary': 6500}
}
sample_dict['emp2']['salary'] = 10000
print(sample_dict)