# coding=utf-8
# 3.31作业  - 天气.py
# 2019/4/3 13:55
import json
f =open(r'C:\Users\Lenovo\PycharmProjects\Python\0331\weather.json',encoding='u8')
d = json.load(f)
print(d['forecast'][3])
f.close()