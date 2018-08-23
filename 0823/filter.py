#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
def is_odd(n):
    return n%2==1
print(list(filter(is_odd,[1,2,3,4,54,56,76,8,10])))
'''

def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty,['A','b','','E'])))

