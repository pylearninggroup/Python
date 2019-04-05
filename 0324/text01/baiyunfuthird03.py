

while True:
    a = int(input("请输入a："))
    b = int(input("请输入b："))
    c = int(input("请输入c："))
    jieguo=b*b+4*a*c
    if (a != 0 and jieguo >= 0):
        def solve(a, b, c,):
            x1 = (-b + (b * b - 4 * a * c)**0.5) / (2 * a)
            x2 = (-b - (b * b - 4 * a * c)**0.5) / (2 * a)
            return x1,x2
            print("方程的实根为：", solve(a, b, c))
        break
    else:
            print("您输入的参数有误，请重新输入！")
    continue

# TODO：似曾相似……