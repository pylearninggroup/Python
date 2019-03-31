f=open('123.txt','w',encoding='u8')
f.write('纵有疾风起，人生不言弃')
a=input()
if a=='q':
    f.close()
else:
    print('你忘记关文件啦，快输入q')
