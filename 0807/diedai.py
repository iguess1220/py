from collections import Iterator
L=[]
D={}
S='str'
I=123
T=()
print(isinstance(L,Iterator))
L=[x for x in L]
print(isinstance(D,Iterator))
print(isinstance(S,Iterator))
print(isinstance(I,Iterator))
print(isinstance(T,Iterator))
L=iter(L)
D=iter(D)
S=iter(S)
#iter(I)
T=iter(T)
print(isinstance(L,Iterator))
print(isinstance(D,Iterator))
print(isinstance(S,Iterator))
print(isinstance(T,Iterator))