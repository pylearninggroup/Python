#coding=utf-8
from math import pi

# TODO：默认参数，吼？
def volume(a=3):
    # TODO：应该用float
    return (4/3)*pi*int(a)**3

print('体积为%s'%volume(a=3))

#input写的运行不出来 咋整 需要float转换
# TODO：需要进行异常处理