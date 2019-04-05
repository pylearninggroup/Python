# coding=utf-8
# 3.31作业  - 天气.py
# 2019/4/3 13:55
import json
f =open(r'../weather.json',encoding='u8')
d = json.load(f)
print(d['forecast'][3])
f.close()

# TODO：输出格式稍微差一点点哦，要更人性化一下