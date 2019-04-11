# coding=utf-8
# Python  - HW7.py
# 2019/4/11 18:37
f = open('words.txt',encoding='utf-8')
a=f.read()
f.close()
b=input('input:')
if b in a:
    print('freedom')
else:
    print("Human Rights")
