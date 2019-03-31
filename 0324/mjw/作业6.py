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
       print(put(key))

