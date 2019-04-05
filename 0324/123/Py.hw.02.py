# coding=utf-8
# untitled3  - Py.hw.02.py
# 2019/3/27 21:28
import random
Number =random.randint(1,20)
print('begin')
In = 100
while In != Number:
    In=int(input('guess a number'))
    if In > Number:
        print("a little bigger")
    elif In < Number:
        print("a little smaller")
else:
    print("Bingo")


# 思路没问题，赞👍