L=['hello',1,2,4,'hello']
L.remove('hello')
print(L)
""" while True:
  if 'hello' in L:
    L.remove('hello')
  else: 
     print(L)
     break """

""" L.append('hehe')
print(L)
del L[3] # 删除列表里的第四元素
print(L)
a = 10
del a # 删除变量
type(a) """

#pop  弹出最后一个，设定索引就删除一个索引，取返回值就是已删除的值
result = L.pop() # 默认删除最后一个
print(result) # 返回已删除的那个元素
print(L)
L.pop(0) # 根据索引删除
print(L)


#clear 清空列表
L.clear()
print(L)