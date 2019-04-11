# coding=utf-8
# Python  - HW5.py
# 2019/4/11 17:04
f = open("Half a day.txt", "r",encoding='u8').read()
words_num = len(f.split())
print('单词数量：{words_num}'.format(words_num=words_num))
