#!/usr/bin/env python3
# -*- coding:utf-8 -*-

print(sorted([12,34,56,-33],key=abs))

print(sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower))
print(sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower,reverse=True))