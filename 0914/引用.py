# a = 10 
# b = 10
# print(id(a))
# print(id(b))

# a = [1,2,3] 
# b = a
# c = [1,2,3] # c 赋值是另外引用地址，
# a.append(3)
# print(id(a))
# print(id(b))
# print(id(c))


# 在Python解释器中，对会字符串和数字进行缓存
# 小数字缓存： -5~256 之间的数字，启动时就有，包括三种模式，文本，交互，ide。 大数字缓存： 交互模式没有，其他都有
# a = 10 
# b = 10

# print(id(a))
# print(id(b))

a = 10000
b = 10000 

print(id(a))
print(id(b))


# 字符串缓存的位数默认最大为20位






