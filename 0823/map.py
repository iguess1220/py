#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

def f(x):
    return x*x
'''
L=map(f,[1,2,3,4,5,6,7,8,9,10])
'''
'''
生成列表
'''
def test(f):
  L=[]
  for i in [1,2,3,4,5,6,7,8,9,10]:
    L.append(f(i))
  print(L)
'''
生成迭代器
'''
def test2(z):
   return (z(i) for i in [1,2,3,4,5,6,7,8,9,10])
r=test2(f)
#next(r)
for n in r:
   print(n)

