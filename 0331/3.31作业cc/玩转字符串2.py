# coding=utf-8
# 3.31作业  - 玩转字符串2.py
# 2019/4/3 13:24
str = 'What is dead may never die'
str1 = str.split(' ')
a1 = str1[0]
a2 = str1[1]
a3 = str1[2]
a4 = str1[3]
a5 = str1[4]
a6 = str1[-1]
b1 = a1[0]
b2 = a1[1]
b3 = a1[2]
b4 = a1[-1]
c1 = a2[0]
c2 = a2[-1]
d1 = a3[0]
d2 = a3[1]
d3 = a3[2]
d4 = a3[-1]
e1 = a4[0]
e2 = a4[1]
e3 = a4[-1]
z1 = a5[0]
z2 = a5[1]
z3 = a5[2]
z4 = a5[3]
z5 = a5[-1]
x1 = a6[0]
x2 = a6[1]
x3 = a6[-1]
list1 = [b1 + '\n',b2+'\n',b3+'\n',b4+'\n']
list2 = [c1+'\n',c2+'\n']
list3 = [d1+'\n',d2+'\n',d3+'\n',d4+'\n']
list4 = [e1+'\n',e2+'\n',e3+'\n']
list5 = [z1+'\n',z2+'\n',z3+'\n',z4+'\n',z5+'\n']
list6 = [x1+'\n',x2+'\n',x3+'\n']
f1 = open('玩转字符串2.txt','w',encoding='utf-8')
f1.writelines(list1)
f1.writelines(list2)
f1.writelines(list3)
f1.writelines(list4)
f1.writelines(list5)
f1.writelines(list6)
f1.close()