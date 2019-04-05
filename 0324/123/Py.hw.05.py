# coding=utf-8
# untitled3  - Py.hw.05.py
# 2019/3/28 20:29
def V(r):
    return(4/3)*3.14*r**3
r=float(input('球半径为'))
print(f'V={V(r)}')

# TODO：异常处理，如果输入的是abc那没有做处理