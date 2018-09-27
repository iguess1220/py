
# == 是判断两侧的数据值是否相等

list1 = [1,2]
list2 = [1,2]
result = list1 == list2
print(result)

# is 是判断 两侧的数据是否指向同一空间地址

is_result = list1 is list2
print(is_result)
# 在指向同一地址后结果为true了

list1 = list2
is_result = list1 is list2
print(is_result)

