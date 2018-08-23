#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce

def str2float(arg1):
    var=arg1.split('.')
    return reduce(lambda x,y:x+y/(10**len(var[1])), map(int,var))
print(str2float('112323.445656'))

