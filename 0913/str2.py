""" Str = "helloworld"
# index这个没子字符串会报错,
# index = Str.index('heaa')
# print(index)
# find 方法 ,没有对应值返回 -1 find 和index功能一样，但可避免报错
print(Str.find('heaa'))
print(Str.rfind('l'))  # rfind 可以逆向查询
print(Str.find('l'))  """


# 拆分
""" Str= "hello world"
Str2 = Str.replace('world','chenyang')
print(Str2) #替换 """

# Str1 = 'hello world world world'
# Str3 = Str1.replace('world','python',2)  # 拆开为列表
# print(Str3)

Str1 = 'hello,world,world,world'
result = Str1.split('p',1)
print(result)
Str3 = "17710890916@163.com"
result =Str3.partition("@") # 固定拆分三个，拆开为元组
print(result)


# 连接
str1 = "hello"
str2 = 'world'
result = str1 + "," + str2 
print(result)

# join  --> 符号.join(可迭代对象) 返回结果
list = ['zhangsan','lisi','wangwu']
result = '!'.join(list)
print(result)

