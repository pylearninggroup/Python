def vol():
    return (4 / 3) * pi * int(r) ** 3


pi = 3.14
r = input("请输入半径：")

try:

    print("体积是%s" % vol())
except Exception:
    print('输入的不是数字')