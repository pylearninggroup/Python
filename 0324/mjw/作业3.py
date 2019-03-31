#一元二次方程
import sys
a=float(input())
b=float(input())
c=float(input())
zbc=b*b-4*a*c
if zbc>=0:
   x1=(-b+(b*b-4*a*c)**0.5)/(2*a)
   x2=(-b-(b*b-4*a*c)**0.5)/(2*a)
   print(x1,x2)
elif zbc<0:
    sys.exit()
