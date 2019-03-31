#猜数字
import random
import sys
result=random.randint(1,20)

while True:
   s= int(input("猜测值"))
   if s<5:
       print("猜小啦！")
   elif s>5:
        print("猜大啦！")
   elif s==5:
       sys.exit()

