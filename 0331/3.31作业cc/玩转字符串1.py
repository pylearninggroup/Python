# coding=utf-8
# 3.31作业  - 玩转字符串1.py
# 2019/4/3 12:48
str = 'What is dead may never die'
str1 = str.split(' ')
a1 = str1[0]
a2 = str1[1]
a3 = str1[2]
a4 = str1[3]
a5 = str1[4]
a6 = str1[-1]
list = [a1+'\n',a2 + '\n',a3 + '\n',a4 + '\n',a5 + '\n',a6 + '\n']
f = open('玩转字符串1.txt','w',encoding='utf-8')
f.writelines(list)


f.close()
