#!/usr/bin/python
# -*- coding: UTF-8 -*-
#二分法求平方根
#lalala
def sqrt_func(x):
    low = 0.0
    loops = 1
    high = max(x,1)
    while True and loops <= 1000:
        guess = (low + high)/2
        if abs(guess**2 - x) < 1e-6:
            break
        elif guess**2 < x:
            low = guess
        else:
            high = guess

        loops += 1
    return guess,loops

#牛顿法1求平方根
def nuaqrt_func(x):
    y = 1.0#从1开始找些许慢
    while abs(y*y -x)>1e-6:
        y = (y+x/y)/2
    return y

#牛顿法2求平方根
def sqrt_nd(x):
    loops = 1
    low = 0.0
    high = max(x,1)
    guess = (low+high)/2
    while abs(guess**2 -x)>1e-6 and loops<=1000:
        guess = guess - (guess**2-x)/2/guess
        loops += 1
    return guess,loops
