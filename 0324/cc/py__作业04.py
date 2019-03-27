# coding=utf-8
# 3.24崔超作业  - py__作业04.py
# 2019/3/25 21:11
def write():
    f = open(input("请输入文件路径："),'w',encoding='utf-8')
    f.write(input("请输入想写入的内容："))
    f.close()
write()
