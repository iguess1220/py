#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# reduce 作用的函数必须接受两个参数，reduce把结果和序列的下一个元素做累计计算

#累加：
from functools import reduce
def add(x,y):
    return x+y
#print(reduce(add,[1,3,5,7,10]))

# 而sum直接可以做
#print(sum([1,3,5,7,10]))
# 但sum不能把数字变成135710
def test(x,y):
    return x*10+y
#print(reduce(test,[1,3,5,7,9]))

def char2num(s):
    digits={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    return digits(s)
#print(reduce(test,map(char2num,'13457')))


def str2int(s):
    digits={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    def var(i):
        return digits[i]
    return reduce(lambda x,y: x*10+y, map(var,s))
print(str2int('13546'))



















