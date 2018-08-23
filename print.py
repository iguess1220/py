#!/usr/bin/env python3.7
for i in [1,2,3,4,5]:
    print(i)

'''
等价于
'''

i=iter([1,2,3,4,5])
while True:
    try:
        x = next(i)
        print(x)
    except StopIteration:
        break
          