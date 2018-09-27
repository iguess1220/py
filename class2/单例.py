# 单例模式,创建的对象始终为同一个内存地址，也就是只有一个对象

class Dog:

    """自定义new方法，来决定返回值，做判断，如果已创建对象则直接返回已有对象，可以将已有对象赋值给类属性的方式达到目的"""

    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return  cls.__instance

dog1 = Dog()
dog2 = Dog()
print(dog1)
print(dog2)