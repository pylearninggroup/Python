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
    # Remove redundant parentheses 括号是不必要的
    if(a != 0 and root >= 0):
        def solve(a, b, c):
            # 求根公式写错了吧，前面多了个-
            x1 = -(-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
            x2 = -(-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
            return x1, x2
        # print(solve(a,b,c))
        print("方程的实根为：",solve(a,b,c))
        break
    else:
        print("您输入的参数有误，请重新输入！")
    continue


# 有以下几个问题:
# 1. 弱警告
# 2. 我们一般函数定义都是顶格写的，很少会在循环内定义
# 3. 第7行的def solve(a,b,c)很好，直接下面调用就可以了呀