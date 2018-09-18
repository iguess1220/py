# 字典的推导式
#a = { key：value  for 循环}
# dict1 = { i:i**2 for i in range(1,5)}
# print(dict1)

# 互换键值对
dict1 = {"name":'zhangsan','age':20}
dict2 = { dict1[key]:key for  key in dict1}
print(dict2)


list1 = ["beijing","shanghai","chongqin","hangzhou","beijing"]
set1 = { city for city in list1 if not city.startswith('b')}
print(set1)

