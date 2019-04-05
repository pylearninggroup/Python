try:
    from math import pi
    r = float(input('请输入数字'))
    V = (4 / 3) * pi * float(r * r * r)
except ValueError:
    print('输入的值不是数字！')
else:
    print(f'体积是{V}')
finally:
    import sys
    sys.exit()


# 不错，如果把from math import pi放到最开始更好了
