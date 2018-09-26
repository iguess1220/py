class Dog:
    __type = "狗"
    @classmethod   # 固定格式，使用场景，修改或访问类属性时。
    def get_type(cls):
        # 类方法会默认设置第一个形参时cls，相当于self, 自动传递对象就是类对象
        return cls.__type
    @classmethod
    def set_type(cls,name):
        cls.__type = name
        return "设置为：%s" % cls.__type

    @staticmethod  # 即不用类对象也不用实例对象传递参数时，可使用静态方法，减少性能损耗
    def introduce():
        return None
    @staticmethod
    def eat():
        print("haha")


# 类对象和实例对象都可以调用类方法
dog1 = Dog()

dog1.set_type("神仙")
print(Dog.get_type())
Dog.introduce()