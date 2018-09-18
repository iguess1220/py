# list1 = []
# for i in range(1,101):
#     list1.append(i)
# print(list1)


# list1 = [ i for i in range(1,101) ]
# print(list1)

# list2 = [i*i for i in range(5)]
# print(list2)



#支持判断
# list2 = [i*i for i in range(1,11) if i%2 == 0]
# print(list2)

# 列表包含出10个666
list1 = [666 for _ in range(10)]
print(list1)

# 过滤列表
list1 = ["zhangsan","lisi","wangwu"]
list2 = [name for name in list1 if len(name) > 5]
print(list2)