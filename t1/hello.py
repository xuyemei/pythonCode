# print('hello word','123','ddd')
# print(122+456)
# name = input()
# print('my name is ',name)
# birth = input()
# birth = int(birth)
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')
# names = ['a','b','c','d']
# sum = 0
# for x in [1,2,3,4,5,6,7,8,9]:
#     sum += x
# print(sum)
# print(list(range(5)))
# sum = 0
# for x in list(range(101)):
#     sum +=x
# print(sum)
#dic
# d={'aa':1,'bb':2,'cc':3}
# print(d.pop('aa'))
# print(d)

#set
# s=set([1,2,3,1,2])
#
# s.add(4)
# s.add(3)
# print(s)
# s1=set([1,2,3])
# s2=set([2,3,4])
# s1.add([1,2])
# print(s1)

# a='abc'
# b=a.replace('a','A')
# print(a)
# print(b)
#
# t=(1,2,3,3)
# t1=(1,2,[3,4])
# d={'a':t,'b':t1}
# s=set(t)
# print(d)
# print(s)

# a=10
# b=hex(a)
# print(b)

# def my_abs(num):
#     if not isinstance(num,(int,float)):
#         raise TypeError('bad operand type for my_abs():')
#     if num > 0:
#         return num
#     else:
#         return -num
#
#
# # print(my_abs('a'))
#
# my_abs('a')
import math
# def quadration(a,b,c):
#     if a == 0:
#         return False
#     x1 = (-b+math.sqrt(b*b+4*a*c))/(2*a)
#     x2 = (-b-math.sqrt(b*b-4*a*c))/(2*a)
#     return x1,x2
#
# print(quadration(2, 3, 1))

# def power(x,n=2):
#     s=1
#     while n > 0:
#         s = s*x
#         n = n-1
#     return s
#
# print(power(3,3))

# def add_end(L=None):
#     if L is None:
#         L=[]
#     L.append('END')
#     return L
#
# print(add_end())
# print(add_end())
# print(add_end())

#可变参数
# def calc(*nums):
#     s = 0
#     for i in nums:
#         s = s+ i*i
#     return s
# print(calc(*[1,2,3]))
# print(calc(1,2,3,5))

#关键字参数
# def person(name,age,**kw):
#     print('name:',name,"age:",age,"other:",kw)
#
# person('yemei',30)
# person('yemei1',30,city='shagnhai',job='php')

# def f(a,b,c=0,*args,city='sss',**kw):
#     print(a,b,c,args,city,kw)
#     pass
# f(1,2,3,[456,789],city='sh')

def pro(*args):
    s = 1
    for i in args:
        s = s*i
    return s
print(pro(5,6))