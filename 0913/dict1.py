d = {'name':'cy','age':18,'city':'beijing'}

# 直接根据键取值
# print(d['name'])
#get 取值不报错
# print(d.get('new_name',123))
# 改为视图对象，Python2中为列表。 为节省内存 , 1,可查看内部结构，2.进行for遍历 3 用in 进行判断 4, 可转换成高级变量类型
import sys
keys = d.keys()
key_list = list(keys)
print(sys.getsizeof(keys))
print(sys.getsizeof(key_list))
for i in keys:
    print(i)
# for value in d.values():
#     print(value)

# for item in d.items():
#     print(item)

#利用自动解包

# for key,value in d.items():
#     print(key)
#     print(value)
# 直接遍历字典和keys一样的效果
# for i in d:
#     print(i)