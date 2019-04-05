# coding=utf-8
# 3.31作业  - 列表推导.py
# 2019/4/1 19:50
# for循环简单实现
a = []
L = list(range(1,101))
for i in L:
    c = L[6::10]
    # TODO：c已经是我们想要的结果了
    a.append(c)
print(a)
# 列表推导实现
L = list(range(1,101))
a=[i for i in L[6::10]]
print(a)
