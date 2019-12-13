#!/usr/bin/env python3
# -*- coding:utf-8 -*-


L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s,str)]
print(L2)

print([x*x for x in range(1,11)])
print([x*x for x in range(1,11) if x %2 == 0])
print([m+n for m in 'ABC' for n in "xyz"])
d={'x':"A",'y':'B','z':'C'}
print([k +'='+v for k,v in d.items()])

#列出当前目录下的所有文件和目录

import os
d = [d for d in os.listdir('.')]
print(d)