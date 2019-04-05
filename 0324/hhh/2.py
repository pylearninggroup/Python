import random
a=random.randint(1, 20)
b=int(input())
if a<b<=20:
    print('大啦')
elif 1<b<a:
    print('小啦')
else:
    # TODO：注意IDE的警告，Python是强类型的语言，不允许数字和字符串相加
    # TODO：这里需要用一种格式化字符串的方法
    print('恭喜你猜对了，该数字为'+b)
    import sys
    sys.exit()

# TODO：需要使用循环哦