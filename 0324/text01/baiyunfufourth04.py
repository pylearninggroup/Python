def write():
    f = open(input("请输入文件路径："), 'w', encoding='utf-8')
    f.write(input("请输入想写入的内容："))
    f.close()


write()
