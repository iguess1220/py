class Dog:
    def __init__(self):
        self.__age = None # 添加两个下划线设置为私有属性，只能类内可用，类外部无法赋值和访问
    def set_age(self,age):
        if age >= 0:
            self.__age = age
        else:
            self.__info("age")
    def get_age(self):
        return self.__age
    def __info(self,property_name): # 设置方法，只能在类内部调用
        print("%s 属性赋值失败" % property_name)
dog1 = Dog()
# dog1.age = -10  #为了防止不规范数据,不直接赋值属性,通过设置方法来实现赋值，可在方法里进行条件判断筛选数据
dog1.set_age(-10)

# print(dog1.get_age())
# print(dog1.__age) #

