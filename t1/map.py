#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def f(x):
    return x*x
r = map(f,[1,2,3,4,5,6,7,8,9])

print(list(r))

print(list(map(str,[1,2,3,4,5,6,7,8,9])))

from functools import reduce
digist = {'0':0,'1':1,'2':2,'3':3,"4":4,'5':5,'6':6,'7':7,'8':8,'9':9}
def str2int(s):
    def fn(x,y):
        return x*10 + y
    def char2num(s):
        return digist[s]
    return reduce(fn,map(char2num,s))
print(str2int('1234567'))

def char2num(s):
    return digist[s]

def str2int(s):
    return reduce(lambda x,y:x*10+y,map(char2num,s))