# coding=utf-8
# Python  - HW8.py
# 2019/4/11 18:52
f = open('words.txt',encoding='utf-8')
a=f.read()
f.close()
b=input('input;')
for b in a:
    a = a.rstrip()
    if b in a:
        a_len = len(a)
        b = b.replace(a, '*' * a_len)

else:
    print(b)
