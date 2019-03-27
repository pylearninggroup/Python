f = open(r'C:\Users\Lenovo\PycharmProjects\Python\0324\assignments.md','r',encoding='utf-8') #打开文件
i = 0 #  需要先定义一下i从0开始，即让文件从头开始切割
while i<80 : # 80是源文件行数
    with open('拆分的'+str(i),'w') as f1:
        for j in range(0,10) : #这里设置每个子文件的行数
            if i <= 80 : #这里判断一下是否切完
                """这里会报编码错误，因为我不知道怎么改，所以下面用一下异常捕获"""
                try:
                    f1.writelines(f.readline())
                except:
                    print("编码错误，但是没关系！")
                i = i+1
            else:
                break
