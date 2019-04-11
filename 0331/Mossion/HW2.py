# coding=utf-8
# Python  - HW2.py
# 2019/4/11 12:29
b = range(1,20000001)
num_list=list(b)

a={}
a=a.fromkeys(b)
import time
t0=time.time()
num_list.index(1000000)
t1=time.time()-t0
print(t1)
t2=time.time()
print(a[2000000])
t3=time.time()-t2
print(t3)