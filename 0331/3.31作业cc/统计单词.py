# coding=utf-8
# 3.31作业  - 统计单词.py
# 2019/4/1 20:11
'''这题不会啊
就能写到这
用正则是不是很简单
然而咱们没学过正则啊
老师'''
# TODO: 是的，用正则很好，但是想一想，英文分词靠的是空格
# TODO: 直接把文件读出来，用空格分割，统计列表长度就对了
f = open('Half a day.txt','r',encoding='utf-8')
readline = f.readlines()
word = []
for line in readline:
    line = line.replace('',',')
    line = line.strip()
    wo = line.split(' ')
    word.extend(wo)
    print(word)