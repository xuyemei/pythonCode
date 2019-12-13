#!/usr/bin/env python3
# -*- coding:utf-8 -*-


#int 是值类型，list 是引用类型
a = 1
b = a
a = 2
print(b)#1

aa = [1,2,3,4]
bb = aa
aa[0] = 'a'
print(bb)#['a',2,3,4]

#值类型：str int tuple 不可变
#引用类型：list set dict  可变