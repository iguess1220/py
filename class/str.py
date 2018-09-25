# class Dog:
#     def __init__(self, *args, **kwargs):
#             self.name = args
#     def __str__(self): # str方法是在对象被输出时调用，return返回值必须为字符串
#             return "我是 %s" % self.name
# dog1 = Dog("旺财")
# print(dog1)
import time

class Potato:
    """地瓜类"""
    def __init__(self):
        self.state = '生的'
        self.cooked_time  = 0
        self.condiment = []
    def cook(self,time):
        self.cooked_time += time
        if 3 > self.cooked_time >= 0 :
            self.state = "生的"
        elif 3 <= self.cooked_time < 6:
            self.state = "半生不熟"
        elif 6 <= self.cooked_time < 8:
            self.state = "输了"
        else:
            self.state = "烤糊了"
    def add_condiment(self,condiment):
        self.condiment.append(condiment)
    def __str__(self):
        # 不知道是什么类型时可用%s,会完成自动转换，自己把列表转换字符串可以用 ','.join() 方法
        return "地瓜状态：%s, 烧烤总时间: %s，加了的调料有: %s" % (self.state, self.cooked_time,','.join(self.condiment))
        # 下边的会输出列表
        #return "地瓜状态：%s, 烧烤总时间: %s，加了的调料有: %s" % (self.state, self.cooked_time,self.condiment)

digua1 = Potato()
digua1.cook(2)
digua1.add_condiment("盐")
digua1.add_condiment("辣椒")
print(digua1)