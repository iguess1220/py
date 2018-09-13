#大小写转换
a = 'Hello,world'
""" result = a.upper()
print(result)
result = a.lower()
print(result) """


# 将字符串放在中心 center

# result = a.center(50,'=')
# print(result)



# 去除字符串两边的空格: strip rstrip右边的 lstrip左

b = '  hello world  '
#result = b.strip()
#result = b.rstrip()
#print(result)
b = '==hello=world'
result = b.strip("d") # str.strip("=") 默认是去除空格，指定去除的内容
print(result)


""" res1 = b.replace(' ','')
print(res1) """