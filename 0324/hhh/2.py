import random
a=random.randint(1, 20)
b=int(input())
if a<b<=20:
    print('大啦')
elif 1<b<a:
    print('小啦')
else:
    print('恭喜你猜对了，该数字为'+b)
    import sys
    sys.exit()
