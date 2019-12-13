#!/usr/bin/env python3
# -*- coding:utf-8 -*-

l1 = ('aaa','bbb','ccc','ddd')
l2 = ('aaa2','bbb2','ccc2','ddd2')

print(l1 +l2)#['aaa', 'bbb', 'ccc', 'ddd', 'aaa2', 'bbb2', 'ccc2', 'ddd2']

print(l1*2)#['aaa', 'bbb', 'ccc', 'ddd', 'aaa', 'bbb', 'ccc', 'ddd']

print(3 in [1,2,3,4])#True
print(3 not in [1,2,3,4])#False
print(3 in (1,2,3,4))#True

print(len([1,2,3]))#3
print(len((1,2,3,5)))#4
print(len('hello'))#5

print(max([1,2,3,4,5]))#5
print(max((1,2,3,4,5)))#5
print(max('hello world'))#w

print(min([1,2,3,4,5]))#5
print(min((1,2,3,4,5)))#5
print(min('helloworld'))#w