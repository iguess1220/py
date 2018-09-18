# set 的主要作用就是去重复
# 大括号内不是键值对的，就是集合
a = {1,2,3,3,4}
print(a)
print(type(a))
list1 = [1,2,3,4,5,4,3,2]
print(list1)
list2 = list(set(list1))
print(list2)

