# coding=utf-8
# 3.31作业  - 从小到大排列.py
# 2019/4/1 19:47
a = int(input("请输入数a："))
b = int(input("请输入数b："))
c = int(input("请输入数c："))
if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    c, b = b, c
print(a,b,c)


# TODO：这个，假如用户输入的一百个数字呢？
# TODO：比较好的思路是，把用户输入的值放到列表里（记得转换类型），然后sort一下