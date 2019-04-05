# coding=utf-8
from math import sqrt
def hahaha(a,b,c):
    # TODO：这里你是返回了两个字符串，不是表达式
    # 以及最后的2*a，应该是（2*a）
    return('x1=(-b+b**0.5-4*a*c)/2*a',"x2=(-b-b**0.5-4*a*c)/2*a")
# TODO：应该用float
a=int(input('a'))
b=int(input('b'))
c=int(input('c'))
print(hahaha(a,b,c))
