#!/usr/bin/env python3
# -*- coding:utf-8 -*-

account = 'yemei'
password = '123456'

print('please input name')
user_name = input()

print('please input password')
user_pass = input()

if user_name == account and user_pass == password:
    print('yes')
else:
    print('no')
