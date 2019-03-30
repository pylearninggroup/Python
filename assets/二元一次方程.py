import math
def equation(a,b,c):
    mid = b**2-4*a*c
    if mid>=0:
        x1 = (-b+math.sqrt(mid))/2*a
        x2 = (-b-math.sqrt(mid))/2*a
        print('x1 = %.2f'%x1,'x2=%.2f'%x2)
    else:
        print('No valid result')

print('Please enter the coefficients')
print('the formula should be ax^2+bx+c ')
equation(a=int(input()),b=int(input()),c=int(input()))