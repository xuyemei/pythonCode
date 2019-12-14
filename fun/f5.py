#函数
import sys
sys.setrecursionlimit(10000)#设置递归的最大次数

def fun1(param1,param2):
    res1 = param1 * 2
    res2 = param2 + res1
    return res1,res2

result1,result2 = fun1(2,3)
print(result1,result2)