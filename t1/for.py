#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from collections import Iterable,Iterator
print(isinstance('acv',Iterable))
print(isinstance([1,2,3],Iterable))

def g():
    yield 1
    yield 2
    yield 3

print('Iterable?[1,2,3]:',isinstance([1,2,3],Iterable))
print('Iterable?\'abc\':',isinstance('abc',Iterable))
print('Iterable? 123:',isinstance(123,Iterable))
print('Iterable? g():',isinstance(g(),Iterable))

print('Iterator?[1,2,3]:',isinstance([1,2,3],Iterator))
print('Iterator?iter([1,2,3]):',isinstance(iter([1,2,3]),Iterator))
print('Iterator?\'abc\':',isinstance('abc',Iterator))
print('Iterator? 123:',isinstance(123,Iterator))
print('Iterator? g():',isinstance(g(),Iterator))

for x in [1,2,3,4,5]:
    print(x)

for x in iter([1,2,3,4,5]):
    print(x)

#print(next():)
it = iter([1,2,3,4,5])
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

d={'a':1,'b':2,'c':3}
for k in d.keys():
    print('key:',k)

for v in d.values():
    print('value:',v)

for k,v in d.items():
    print('item:',k,v)

#使用迭代查找一个list中最小和最大值，并返回一个tuple
def findMinAndMax(L):
    pass
    r = sorted(L)
    le = len(r)
    t = []
    for i,v in enumerate(r):
        if i == 0 :
            t.append(v)
        if i == le-1:
            t.append(v)
    return t
print(findMinAndMax([1,3,5,2,4]))