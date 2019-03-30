# coding=utf-8
import sys

qh = {
    '010': 'Beijing',
    '021': 'Shanghai',
    '024': 'Shenyang',
    '0411': 'Dalian',
    '0247': 'Tieling',
    '0417': 'Yingkou',
    '0352': 'Datong',
}

while True:
    a = input('请输入区号')
    if a == 'q':
        sys.exit()
    else:
        print(input(qh.get(a)))
