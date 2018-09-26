
# 当对象属性不同时，在__init__中定义，若创建的所有对象的某个属性相同，则把这个属性定义为类属性，节省内存


class Dog:
    type = "狗"
    def __init__(self):
        self.name = None
#       self.type = "狗"  这个方式定义较损耗性能，每个实例都定义一次

dog1 = Dog()
dog2 = Dog()

dog1.name = "旺财"
dog2.name = "来福"
print(dog1.type)
print(dog2.type)
