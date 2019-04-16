# coding: utf-8
# course - keys.py
# 2019/4/16 15:27

import json
import time

import requests


def q1():
    # 火箭发射
    count_down = 5
    while count_down > 0:
        print('倒计时%s' % count_down)
        count_down -= 1
        time.sleep(1)
    print('发射')


def q2():
    # 字典和列表的查找速度
    large_list = list(range(1000000))
    large_dict = {}.fromkeys(large_list)

    t0 = time.time()
    large_list.index(500000)
    print(f'time for list {time.time() - t0}')

    t0 = time.time()
    large_dict.get(500000)
    print(f'time for dict {time.time() - t0}')


def q3():
    # 直接应用列表的sort方法就可以了
    content = input('输入数字 空格分隔')
    # 用空格分割字符串，转换成数字
    content = [float(i) for i in content.split()]
    # 排序，如果有必要，指定逆序reverse=True
    content.sort()
    print(content)


def q4():
    # 7结尾数字
    nums = []
    for i in range(100):
        # 转换成字符串，判断是否为7结尾
        if str(i).endswith('7'):
            nums.append(i)
    # 列表推导
    print([i for i in range(100) if str(i).endswith('7')])
    # range也可以，但是这种解法就忽略列表推导吧
    print(list(range(7, 100, 10)))


def q5():
    # 单词数目
    # 打开文件，读取为字符串，按照空格分割为列表，计算列表长度也就是单词数目了
    f = open('Half a day.txt')
    # f.read()读取文件内容为字符串，split()分割，len计算长度
    print(f'单词数目{len(f.read().split())}')
    f.close()


def q6():
    # 只是练习下args、kwargs
    pass
    # def fun(*args,**kwargs):
    #     print(args)
    #     print(kwargs)


def q7():
    # words为列表，每行一个敏感词
    words = open('words.txt', encoding='utf-8').readlines()
    user = input('输入句子')
    # 遍历敏感词列表，word为单行词
    for word in words:
        # 把每个敏感词与用户输入进行比较
        if word.strip() in user:
            print('Freedom')
            break
    else:
        print('Human rigints')


def q8():
    words = open('words.txt', encoding='utf-8').readlines()
    user = input('输入句子')
    # 遍历敏感词列表，word为单行词
    for word in words:
        # 把每个敏感词与用户输入进行比较
        if word.strip() in user:
            # 替换敏感词，然后重新复制给用户输入的内容，因为一句话可能有多个敏感词
            user = user.replace(word.strip(), len(word.strip()) * '*')
            # break
    print(user)


def q9():
    # 按照空格分词，正好分为列表，然后每个单词结尾加上\n
    phrase = 'What is dead may never die'
    # 使用列表推导
    content = [word + '\n' for word in phrase.split()]
    # 使用常规方法
    # content = []
    # for word in phrase:
    #     content.append(word + '\n')
    # 最后的结果
    # ['What\n', 'is\n', 'dead\n', 'may\n', 'never\n', 'die\n']
    with open('result.txt', 'w', encoding='utf-8') as f:
        # writelines写入结果
        f.writelines(content)


def q10():
    # 同上，只不过没有给phrase.split()
    phrase = 'What is dead may never die'
    content = [word + '\n' for word in phrase]  # here
    with open('result.txt', 'w', encoding='utf-8') as f:
        # writelines写入结果
        f.writelines(content)


def q11():
    # post的数据是fruits=grape
    for i in range(1000):
        requests.post('http://115.159.180.177:5022/', data=dict(fruits='grape'))
    # 其实这里有加速的方法，包括连接复用（session）、多线程


def q12():
    # 使用json.load反序列化字符串为字典
    data: dict = json.load(open('weather.json', encoding='utf-8'))

    print(f'''
    城市：{data['city']}
    穿衣指数：{data['tip']}
    日期：{data['forecast'][3]['date']}
    天气：{data['forecast'][3]['type']}
    气温：{data['forecast'][3]['temp']}
    日出：{data['forecast'][3]['sun_rise']}
    日落：{data['forecast'][3]['sun_down']}
    '''
          )


if __name__ == '__main__':
    q1()
    q2()
    q3()
    q4()
    q5()
    q6()
    q7()
    q8()
    q9()
    q10()
    q11()
    q12()
