#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

def abstest(n):
    if not isinstance(n,(int,float)):
        raise TypeError("bad operand type")
    if n >= 0 :
        return n
    else:
        return -n

