# coding=utf-8
# 3.24崔超作业  - py__作业03.py
# 2019/3/25 18:39
# 二元一次方程组求解
import math
from math import sqrt
# def solve(a,b,c):
#     x1 = (-b + math.sqrt(b * b -4 * a * c))/(2 * a)
#     x2 = (-b - math.sqrt(b * b -4 * a * c))/(2 * a)
#     return x1,x2
while True:
    a = int(input("请输入a："))
    b = int(input("请输入b："))
    c = int(input("请输入c："))
    root = b*b - 4 * a * c
    if(a != 0 and root >= 0):
        def solve(a, b, c):
            x1 = -(-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
            x2 = -(-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
            return x1, x2
        # print(solve(a,b,c))
        print("方程的实根为：",solve(a,b,c))
        break
    else:
        print("您输入的参数有误，请重新输入！")
    continue
