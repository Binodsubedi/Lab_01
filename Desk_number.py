import math

Stu_1 = int(input('Enter the number of students in class 1:'))
Stu_2 = int(input('Enter the number of students in class 2:'))
Stu_3 = int(input('Enter the number of students in class 3:'))

num1 = math.floor(Stu_1/2)
num2 = math.floor(Stu_2/2)
num3 = math.floor(Stu_3/2)

print(f'The possible combination to the least number is {num1}, {num2}, {num3} respectively')

