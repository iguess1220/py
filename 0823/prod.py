#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce
def prod(list_first,list_second):
    return  list_first*list_second
a=reduce(prod,[3,5,7,9])
print(a)
