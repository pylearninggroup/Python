a=int(input())
b=int(input())
c=int(input())
from math import sqrt

# TODO：这里，差一点点
#def
# TODO：百分号是取余数呀
x=(-b+sqrt(b*b-4*a*c))%(2*a)
y=(-b-sqrt(b*b-4*a*c))%(2*a)
print(x,y)