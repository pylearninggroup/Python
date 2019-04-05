# coding=utf-8
# 3.31作业  - 敏感词1.py
# 2019/4/2 19:53
from sys import argv   #  接受命令行传进来的参数
# 1.先将txt文件中的内容存到一个列表里


def fun1():
    words = []      # 这里定义一个空列表盛装敏感词
    f = open('word.txt',encoding='utf-8')   # 打开文件
    for word in f:   # 遍历文件中的词汇
        words.append(word[:-1])     # 将敏感词汇添加到空列表中
    f.close()
    return words           # 返回列表words


# 2.判断输入的内容是否包含在列表里
def fun2(words, b):
    """

    :param words: 之前盛装敏感词的列表
    :param b: 用户输入的信息
    :return:
    """
    b = input("请输入信息：")       # 获取用户输入
    for w in words:
        if w == b:        # 判断用户输入是否包含在列表内
            print("freedom")
            return
    print("Human Rights")
    return
fun2(fun1(),input)
