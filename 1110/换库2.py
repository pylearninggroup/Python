# coding=utf-8
# 课程作业  - 换库2.py
# 2019/11/16 11:01
import pymongo
import pymysql

con = pymysql.connect(host='shemissed.me', port=33060, user='root',
                      password='bennythink', database='board', charset='utf8mb4')
cur = con.cursor()
cur.execute('select * from cc')
data = cur.fetchall()
# print(data)
# dataset = []

client = pymongo.MongoClient()
db = client['hello']
col = db['cc']
result = []
for item in data:
    name = item[0]
    msg = item[1]
    dt = item[2]
    ip = item[3]
    # print(name,msg,dt,ip)

    result.append({'姓名': name, '留言': msg, '时间': dt, 'IP': ip})
col.insert_many(result)
# col.insert({'姓名': name, '留言': msg, '时间': dt, 'IP': ip})
# database = list(col.insert(data))
client.close()

s = 'aaa'
