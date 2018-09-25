# class Dog:
#     """python会隐式的把调用方法的对象，作为第一个实参传递，在方法中使用对象的属性时，用self来访问"""
#     def introduce(self):
#         print("我是%s,请多多关照" % self.name)  # self 将调用这个类的对象自己，即dog1 /dog2 作为参数传递进来

# dog1 = Dog()
# dog2 = Dog()

# dog1.name = "旺财"
# dog2.name = "来福"

# dog1.introduce()
# dog2.introduce()

""" 关于__init__"""

class Dog:
    def __init__(self,name): # __xx__()魔法方法 (运算符重载方法)，都具有特殊含义，在特殊情况下会自动调用
        self.name = name # 一般用于定义对象的初始操作，如定义属性
    def introduce(self):
        print("我是%s,请多关照" %self.name)
dog1 = Dog("Mike")
dog2 = Dog("Alan")
dog1.introduce()
dog2.introduce()