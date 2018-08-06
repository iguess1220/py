#L=list(range(1,100))
#print(L)
'''
L=[]
for x in range(1,10)
   L.append(x)
print(L)
'''
L=[x*x for x in range(1,10)]
print(L)
'''
添加判断，不需要截断符号
'''
L=[x*x for x in range(1,10) if x%2==0]
print(L)
'''
两层嵌套循环，生成全排列
'''
L=[m+n for m in 'abc' for n in 'ABC']
print(L)

'''
列出当前目录下的文件
'''
import os
L=[d for d in os.listdir('.')]
print(L)

'''
调用字典的key value 并组合列出
'''
d={'a':'A','b':'B','c':'C'}
L=[k +'='+ v for k,v in d.items()]
print(L)

'把所有字母变小写和大写'
L=['Hello','World','IBM','Apple']
print([s.lower() for s in L])
print([s.upper() for s in L])


'''
练习,使lower()函数执行时跳过不可执行元素，避免报错
'''
L1=['Hello','World',18,'Apple',None]
L2=[s.lower() for s in L1 if  isinstance(s,str)]
print(L2)