#!/usr/bin/env python3
# -*- coding: utf-8 -*-

L=['adam', 'LISA', 'barT']
def normalize(name):
    return str.title(name)
a=map(normalize,L)
print(list(a))
