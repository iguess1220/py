# 多态 当需要使用父类对象的地方，使用子类对象也可以
# 鸭子类型 并不强制要求数据类型，只要数据完成了需要的处理，就可执行

class meat:
    def __init__(self):
        self.name = "肉"
class ham:
    def __init__(self):
        super().__init__()
        self.name = "火腿"
class person:
    def eat(self,meat):
        print("吃：%s" % meat.name)

class potato:
    def __init__(self):
        self.name = "地瓜"

digua = potato()
p1 = person()
h1 = ham()
p1.eat(h1)
p1.eat(digua) # 鸭子类型，可以不是父子类关系，只要都有self.name这个属性就可以使用，动态语言的特性
