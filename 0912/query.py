a=[1,2,3,4,5,6,7,1,2]
""" print(a)
b=lambda x,y: x+y
print(b(1,2)) """
""" print(a) 
b=a.index(4) #根据值获取索引
c=a.index(1) # 重复值取匹配的第一个
print(c)
count=a.count(1) # 值在列表出现的次数
print(count) """
element=len(a)
print(element)
if 10 in a:
    print("包含了")
else:
    print("10")
    