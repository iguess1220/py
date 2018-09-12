""" list=["hello",1.5,10,'chenyang']
print(list)

list2=[1.5,2,10,44]

list2.reverse() #逆序
print(list2) 

list2.sort() #默认升序
print(list2)
list2.sort(reverse=True) #降序
print(list2) """


list=["1",21,3,67,1.5]
list.sort(key=int,reverse=True) #以整数形式排降序
print(list)
list1=["hello",'chenyang','nihaoadada'] #以元素长度来排序
list1.sort(key=len,reverse=False)
print(list1)

