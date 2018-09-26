class Dog:
    def __init__(self):
        self.type = "狗" # 公有属性可以被继承
        self.__age = 10 # 私有属性不能被继承
    def __eat(self): # 私有方法不会被继承
        print("吃东西 ")

class xtq(Dog):
    def __init__(self): # 当前类调用init方法时，重写了父类的init，想要调用父类，须手动添加调用：
        #Dog.__init__(self)
        super().__init__() # super(指定类‘默认为当前类’,对象‘默认self’).方法
        self.color = "黑"
    def do(self):
        print(self.type)


dog1 = xtq()
print(dog1.type)
print(dog1.color)