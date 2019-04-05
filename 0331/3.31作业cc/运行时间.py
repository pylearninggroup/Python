# coding=utf-8
# 3.31作业  - 运行时间.py
# 2019/4/1 19:11
"""跪求老师原谅
我还是菜
代码有点多
其实都一样
"""
import time
list_1 = list(range(1, 10000001))
dict_1 = dict.fromkeys(range(10000001), None)
t1 = time.perf_counter()
print(list_1[999])
t2 = time.perf_counter()
print(t2 - t1)
t3 = time.perf_counter()
print(list_1[49999])
t4 = time.perf_counter()
print(t4 - t3)
t5 = time.perf_counter()
print(list_1[99999])
t6 = time.perf_counter()
print(t6 - t5)
t7 = time.perf_counter()
print(dict_1[1000])
t8 = time.perf_counter()
print(t8 - t7)
t9 = time.perf_counter()
print(dict_1[50000])
t10 = time.perf_counter()
print(t10 - t9)
t11 = time.perf_counter()
print(dict_1[100000])
t12 = time.perf_counter()
print(t12 - t11)
