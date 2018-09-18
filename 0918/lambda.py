# 匿名函数
# a = lambda x,y: x+y
# print(a(1,2))


# #定义匿名函数并直接调用
# result =(lambda x,y: x*y)(1,2)
# print(result)


# 传入可变参数， 返回列表生成式，直接调用取值
result = (lambda *x: [i*i for i in x ])(1,2,3,4)
print(result)
# 解包赋值
a,b,c = (lambda *x: [i*i for i in x ])(2,4,6)
print(a)
print(b)
print(c)







