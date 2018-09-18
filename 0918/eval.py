# 列表转换成字符串后再转列表出现的问题
# str1 = "[1,2,3,4]"
# list1 = list(str1)
# 出现的并不时我们要的结果，列表会把字符串所有元素都拆解
# print(list1)
# 使用函数eval可解决
# list2 = eval(str1)
# print(list2)
# 也可以转换字典，整数，浮点数等
# str2 = "{'a':'2','c':'7'}"
# print(eval(str2))


# eval 不要在工作中使用，可自动识别函数并执行，很危险
a = eval(input("please input:  "))
print(a)
#print(__import__('os').getcwd())