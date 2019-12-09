#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# # # #取前3个
# # # r = L[0:3]
# # # print(L[0:3])
# # # print(L[:3])
# # # print(L[-2])
# # # print(L[-2:-1])
# # # print(L[-3:])


L=list(range(100))
print(L[0:10])
print(L[-10:])
print(L[10:20])
print(L[:10:2])
print(L[::5])#取所有，每5个取一个
print(L[:])

#tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：
#字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串：

#利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法
def trim(s):
    pass