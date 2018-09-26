
# 当对象属性不同时，在__init__中定义，若创建的所有对象的某个属性相同，则把这个属性定义为类属性，节省内存


class Dog:
    type = "狗"
#    __type =  "" #类属性也可以设置为私有
    def __init__(self):
        self.name = None
#        self.type = "狼"  # 这个方式定义较损耗性能，每个实例都定义一次，如果和类属性同名，优先调用实例属性

dog1 = Dog()
dog2 = Dog()
# 修改类属性，只能通过类对象修改
Dog.type = "老虎"

# 实例对象不能修改类属性，dog1创建了type实例属性
#dog1.type = "猪"


dog1.name = "旺财"
dog2.name = "来福"
print(dog1.type)
print(dog2.type)
