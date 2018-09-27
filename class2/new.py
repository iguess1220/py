class Dog:
    pass


def Dog_():
    # new方法用来创建对象
    new_obj = Dog.__new__(Dog)
    # 初始化对象
    new_obj.__init__()
    # 返回生成的对象
    return  new_obj
dog1 = Dog()
dog2 = Dog_()
print(dog2)