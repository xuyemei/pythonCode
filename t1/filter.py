#!/usr/bin/env python3
# -*- coding:utf-8 -*-
def is_odd(n):
    return n%2 == 1

print(list(filter(is_odd,[1,2,3,4,5,6,7,8,9])))

def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty,['A','','B',None,'C',' '])))

def main():
    # 生成1000以内的素数
    for n in primes():
        if n < 1000:
            print(n)
        else:
            break

#生成一个奇数序列
def _odd_iter():
    n = 1
    while True:
        n = n+2
        yield n

#定义一个筛选函数
def _not_divisiable(n):
    return lambda x:x%n > 0

#定义一个生成器，不断返回下一个素数
def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisiable(n),it)


if __name__ == '__main__':
    main()

#生成回数