#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b,a+b
        n = n+1
    return 'done'

f = fib(6)
while True:
    try:
        x=next(f)
        print('f:',x)
    except StopIteration as e:
        print('return value:',e.value)
        break


#杨辉三角
def yanghui(n):
    for i in list(range(1,n)):
        newL = []
        if i == 1:
            newL = [1]
        if i == 2:
            newL = [1,1]
        if i > 2:
            for j in list(range(0,i)):
                if j == 0 :
                    newL.append(1)
                if j == i-1:
                    newL.append(1)
                if j > 0 & j < i-1:
                    pass
                    print(L)
                    newL.append(L[j-1] + L[j])
        L = newL
        yield newL



