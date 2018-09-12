#赋值的右侧为多个数据，有自动组包为元组
""" a = 10,20,'heh'
print(type(a))
print(a)
 """

""" a = 10
b = 20
# 交换变量1 临时变量
temp = a
a = b
b = temp
print(a,b)
# 交换变量2 计算公式
a = a + b
b = a - b
a = a - b
print(a,b)
# 交换变量3 ，元组特性
b,a=a,b # 右侧多个数据会自动组包为元组，当左侧被赋值数量和右侧对等时，进行赋值
print(a,b) """


""" 
a = 10
b = 20 
c = 30
c,b,a = a,c,b
print(a,b,c) """








# 进行格式化的处理
""" price,weight = 7.5,8.5
info=(price,weight)
print("单价为%.2f,重量为%.2f" % info) """




# 把列表锁定为元组，不许修改

list = [1,2,3,4,5]
list = tuple(list)
print(list)
print(type(list))