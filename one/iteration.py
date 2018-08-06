
for i in {'a':1,'b':2,'c':3}:
     print(i)
for i in {'a':1,'b':2,'c':3}.values():
     print(i)
for key,value in {'a':1,'b':2,'c':3}.items():
     print(value,key)
'''
导入判断可否迭代的模块,Iterable在python3.8将停用
'''
from collections import Iterable
'''
判断str,list,dict,int是否可迭代
'''
print(isinstance('chenyang',Iterable))
print(isinstance([1,2,3,4],Iterable))
print(isinstance({'a':1,'b':2,'c':3},Iterable))
print(isinstance(1235,Iterable))
'''
如果要迭代list的索引,使用内置函数enumerate(sequence, [start=0])
'''
#L=['a','b','c','d']
#L='asdfiuguy'
L=(1,2,3,4,65,873,45,)
for index,value in enumerate(L,start=10):
    print(index,value)

print('\n\n\n\n\n\nstart')
'''
小练习，通过迭代取出列表的最大和最小值，
'''

def findMinAndMax(L):
    if not isinstance(L,list):
        raise TypeError("bad operand type")
    if L == []:
        return (None,None)
    min,max=L[0],L[0]
    for m in L:
        if m < min:
            min = m
        if m > max:
            max = m
    return (min,max)

if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')


























