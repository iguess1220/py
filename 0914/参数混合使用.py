# def func1(*args,is_print): # 如果默认参数和可变参数混合使用，须把默认参数放后边，负责传实参时会被可变参数接收。且在传实参时须使用关键字参数。
#     print(is_print)
#     print(args)

# func1(1,2,3,is_print=True)


print("zhangsan","lisi","wangwu",sep='^')

# def func2(a,**kwargs): # 形参前加** ，就是标识该形参为字典型可变参数，必须在所有形参的最后面
#     # 可以将多余的参数，包装成字典传给形参
#     print(a)
#     print(kwargs)
# func2(a=1,b=2,c=3)


def fun1(*args,**kwargs):
    print(args)
    print(kwargs)
def fun2(*args,**kwargs):
    fun1(*args,**kwargs) # 传递实参进来，变成 args=(1,2,3) kwargs={'a'=3,'b'=4}   也就是fun1((1,2,3),{'a'=3,'b'=4}) 这是两个可变参数（一个元组，一个字典）传入，都被fun1()的可变参数接收。
fun2(1,2,3,a=3,b=4)


# 在实参前加*,可将tuple list转换格式，也可以装换dict 为**

# def zhuan(a,b,c):
#     print(a)
#     print(b)
#     print(c)
# list1 = [1,2,3]
# tuple1 = (1,2,3)
# dict1 = {'a':10,'b':20,'c':30}


# zhuan(**dict1) # {'a':10,'b':20,'c':30} 在** 后转换为--> a = 10 ,b = 20, c =30
# zhuan(*tuple1)  # (1,2,3) 转换为 1，2，3
# zhuan(*list1) # [1,2,3] 转换为 1,2,3







