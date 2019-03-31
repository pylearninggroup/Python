# coding: utf-8
# untitled-ass1
# 2019/3/3021:29

"""选择困难症
import random
a=random.randint(1,4)
if a==1:
    print ("可乐")
elif a==2:
    print ("雪碧")
elif a==3:
    print("coffee")
else:
    print ("白开水")
"""

''''# 猜数字
import random

a = random.randint(1, 20)
while 1:
    b = int(input("please input a number from 1 to 20"))
    if a > b:
        print("try again,猜小了")
    elif a < b:
        print('try again,猜大了 ')
    elif a == b:
        print('you win')
        break
'''

'''#二元一次方程
import math
a = int(input("输入第一个未知数a"))
b = int(input("输入第一个未知数b"))
c = int(input("输入第一个未知数c"))
m = b ** 2 - 4 * a * c
x1 = 0
x2 = 0
if m > 0:
    x1 = int((-b + m ** 0.5) / 2 * a)
    x2 = int((-b - m ** 0.5) / 2 * a)
    print ('x1=',x1)
    print ('x2=',x2)
elif m == 0:
    x= int(-b / 2 * a)
    print(x)
elif m < 0:
    print("no answer")
'''

'''
#写文件
f = open('E:/123.txt','w', encoding='utf-8')
# f.readline()
f.writelines('bkbubob')
while f.writelines('q'):#体现不出来
    break
f.close()
'''
# from math import pi
# r = input("please input the number:")
# try:
#     f = float(r)
#     v = (4 / 3) * pi * (int(r) ** 3)
#     print("球体体积", v)
# except ValueError:
#     print("输入的不是数字")

'''block={'001':'Beijing','002':'Shanghai','003':'Dalian'}
# while 1:
#     i = input('input a number')
#     if i=="q":
#         break
#     else:
#         print(block.get(i,'查无此数'))
'''

with open('E:\xiaodu\Python\0324\assignments.md','r') as f:
    f.readlines()
    content=read.read()

    print(f.split('\n##'))
