#coding=utf-8


import random
import sys
print('Lets play a game ')
print('Please enter a number between 1-20')
num = int(input())
num2 = random.randint(1,20)
while num!=num2:
    if num>num2:
        print('smaller')
        print('PLease try again')
        num = int(input())
    elif num < num2:
        print('larger')
        print('PLease try again')
        num = int(input())
    if num == num2:
        print('congratulations!')
sys.exit()