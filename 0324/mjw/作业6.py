#区号
d = {'024': '沈阳', '0411': '大连'}


def put(code):

    return d.get(code)


while True:
    key = input("请输入区号")
    if key == 'q':
        print("退出系统")
        break
    else:
        # TODO：注意下这里IDE的警告，缩进要保持一致哦
       print(put(key))

