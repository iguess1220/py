""" import keyword
print(keyword.kwlist)
变量的输出
price = 7.5
weight = 8.5
total_price = price * weight
print("总价为%f" % total_price)
print("总价为%.2f" % total_price)
#.2 为输出小数点后两位
print("总价为%.3f" % total_price)

print("%")
a=12345
#占位6个
print("%6d" % a) """

""" name = "小明"
print("大家好，我的名字叫%s,请大家多多关照" % name)
student_no = 1
# 这个只能补0，其他数字不可以
print("我的学号是%06d" % student_no ) """


price = input("单价为: ")
weight = input("重量为(斤): ")
total_price = float(price) * float(weight)
print("单价为每斤%.1f元,重量为%.1f斤,总价是%.2f元" % (float(price),float(weight),total_price)) 
