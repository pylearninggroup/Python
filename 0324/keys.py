# coding: utf-8
# course - 参考解答.py
# 2019/4/5 10:56
import random
import sys
import math


def q1():
    # 选择困难症
    return random.choice(['苹果', '香蕉'])


def q2():
    # 猜数字
    # 生成1-20随机整数
    number = random.randint(1, 20)
    # 进入死循环
    while True:
        # 由于需要猜对为止，所以要在循环里input
        choice = int(input('输入数字'))
        if choice == number:
            print('猜对了')
            break  # 猜对了break程序，或者sys.exit
        elif choice < number:
            print('小')
        elif choice > number:
            print('大')


def q3(a, b, c):
    """
    一元二次方程，接受三个参数abc
    :param a:
    :param b:
    :param c:
    :return: x1 x2
    """
    # 判断是否有实数解
    delta = b * b - 4 * a * c
    if delta < 0:
        print('没有实数解')
    else:
        # 求根公式不要用错了
        x1 = (-b + delta ** 0.5) / (2 * a)
        x2 = (-b - delta ** 0.5) / (2 * a)
        return x1, x2


def q4():
    # 将用户从input输入的内容写入到123.txt中
    # 需要先进入一个死循环
    while True:
        content = input('请输入内容，q退出')
        if content.lower() == 'q':  # 如果用户输入了q，那么break循环
            break
        else:  # 输入的不是q，写文件，追加模式
            with open('123.txt', 'a', encoding='u8') as f:
                f.write(content)


def q5():
    # 计算球体积，需要注意异常处理
    try:
        # 1. 需要用float转
        # 2. 这一步可能输入abc，这个时候需要用异常处理下
        radius = float(input('输入半径'))
    except ValueError:
        print('输入的值不是数字')
        sys.exit()
    return (4 / 3) * math.pi * radius ** 3


def q6():
    # 根据区号转换城市，同样输入q退出，因此需要死循环
    city = {'010': '北京', '024': '沈阳'}

    while True:
        code = input('输入区号')
        if code.lower() == 'q':
            # 输入值是q 退出程序
            break
        else:
            # 使用get方法，没找到时不会出KeyError，并定义自定义返回值
            print(city.get(code, '没找到对应信息'))


def q7():
    # 处理文件
    read = open('assignments.md', 'r', encoding='utf-8')
    # 先去掉开头的五行，使得文件指针指向第一道题前面
    for i in range(5):
        read.readline()
    # 将文件内容全部读取位字符串
    content = read.read()
    # 使用\n##作为分隔符将字符串分割为列表
    content = content.split('\n##')
    # 第一个元素是空的，删掉
    content.pop(0)
    # 遍历列表
    for question in content:
        # 提取标题，先按换行分割，再按.分割
        filename = question.split('\n')[0].split('. ')[-1]
        # with打开文件，注意filename
        with open(f'{filename}.txt', 'w', encoding='utf-8') as write:
            # write写文件，补全##
            write.write(f'##{question}')
    # 关闭读文件流
    read.close()
