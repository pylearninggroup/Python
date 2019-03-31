# coding=utf-8
# untitled3  - Py.hw.03.py
# 2019/3/27 21:45


def cat(a, b, c):
    delta = b * b - 4 * a * c
    if delta < 0:
        print('无解')
    else:
        m = (-b + (b ** 2 - 4 * a * c)**0.5) / 2 * a
        n = (-b - (b ** 2 - 4 * a * c)**0.5) / 2 * a
        print(f'x1: {m}  x2:{n}')


if __name__ == '__main__':
    a = int(input('a='))
    b = int(input('b='))
    c = int(input('c='))
    cat(a, b, c)
