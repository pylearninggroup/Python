# coding=utf-8
# Python  - HW6.py
# 2019/4/11 18:07
def f(x,**kwargs):
    print(x)
    print(kwargs)
f(1,y=1,a=2,b=3,c=4)
#输出1/n {'y': 1, 'a': 2, 'b': 3, 'c': 4}
def fo(x, *args, y=1):
    print(x)
    print(args)
    print(y)
fo(1, 2, 3, 4, 5)
#输出1/n (2, 3, 4, 5)/n 1
