#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#利用递归计算阶乘
def fact(n):
    if n ==1:
        pass
        return 1
    return n*fact(n-1)
print('fact(1)=',fact(1))
print('fact(5)=',fact(5))
print('fact(10)=',fact(10))


#利用递归移动汉诺塔
def move(n,a,b,c):
    pass
    if n ==1:
        print('move',a,'--->',c)
    else:
        move(n - 1, a, c, b)
        move(1,a,b,c)
        move(n-1,b,a,c)

move(4, 'A', 'B', 'C')