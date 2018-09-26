class Dog:
    def bark(self):
        print("汪汪叫")
    def eat(self):
        print("吃肉")
class god:
    def fly(self):
        print("飞一会儿")
    def eat(self):
        print("吃蟠桃")
class xtq(Dog,god): # 继承类时，相同得方法，选择执行类内方法得顺序 为 写入得参数顺序，即优先执行Dog.eat
    def eat(self):
        god.eat(self) # 多继承中，想要使用指定某个父类得方法，先重写，然后直接调用 使用方式1
        super(Dog,self).eat() # 方式2，多用于直接调用单一父类

xiaotq = xtq()
xiaotq.bark()
xiaotq.fly()
xiaotq.eat()
print(xtq.__mro__) # 查看继承链，可以通过 类名称.__mro__ 这个魔法方法输出