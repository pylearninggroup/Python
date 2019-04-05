#写文件
while True:
    s=input()
    if s=='q' or s=='Q':
        break
    else :
        # TODO：建议用追加模式a
        f=open('123.txt','w',encoding='u8')
        # f.write(s)就对啦
        f.write()
        f.close()
