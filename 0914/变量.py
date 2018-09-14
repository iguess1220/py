# def func1():
#     """局部变量"""
#     a = 10 
#     print(a)


# def func2():
#     print(a)


# 变量 a定义在func1里面,仅在func1内可用,func2一样不能用
#print(a)  
#func1()
#func2() """


# 全局变量
a = 10
def func1():
    global a # 如果要使用全局变量,需要global声明 变量名,在函数的第一行写
    print(a)
    a = 5  # 未声明之前是局部变量,声明后为全局变量
func1()
print(a)