#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def huishu(n):
    s=str(n)
    return s==s[::-1]
a=list(filter(huishu,range(1000)))
#a=filter(huishu,range(1000))
print(a)
