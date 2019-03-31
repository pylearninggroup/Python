import random

a = random.randint(1, 20)
print("请输入你要猜的数字")
b = 0
while a != b:
    c = input()
    b = int(c)
    if b < a:
        print("你输入小了")
    elif b > a:
        print("你输入大了")
else:
    print("猜对了")
