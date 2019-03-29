# coding=utf-8
# 3.24崔超作业  - py__作业02.py
# 2019/3/25 18:31
# 猜数字游戏
import random
# 这里 空格
answer =random.randint(1,21)
print("猜数字游戏开始！")
guess = 0
while guess != answer:
    put = input("请输入你的猜测：")
    guess = int(put)
    if guess < answer:
        print("你可真笨，这都能猜小了？！！")
    elif guess > answer:
        print("你咋这么笨，这都能猜大了？！！")
else:
    print("猜对了，你可真是个小机灵鬼儿！")