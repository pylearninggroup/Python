# coding=utf-8
# 3.24崔超作业  - py__作业05.py
# 2019/3/25 21:55
import math
def vol():
    return (4/3)*pi*int(r)**3
pi = 3.14
r = input("请输入半径：")
if r.isdigit() == True:
    print("体积是%s"%vol())
else:
    print("您输入的值不是数字！")