# coding=utf-8
# Python  - HW3.py
# 2019/4/11 16:51
a = int(input("a："))
b = int(input("b："))
c = int(input("c："))
num_list=[a,b,c]
if a>b:
    num_list=[b,a,c]
if b>c:
    num_list=[c,b,a]
if a>c:
    num_list=[b,c,a]
print(num_list)