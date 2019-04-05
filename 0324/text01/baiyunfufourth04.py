def write():
    f = open(input("请输入文件路径："), 'w', encoding='utf-8')
    f.write(input("请输入想写入的内容："))
    f.close()


write()


# TODO：需要循环
# TODO：追加模式打开文件
# TODO：q退出