#class Animal: 经典类写法
class Animal(object) # 新式类写法，和经典类同效果， object类是系统的类，所有的类都要继承它
    def eat(self):
        print("吃东西")

class Dog(Animal): # 继承的方式：子类(父类/基类)
    def bark(self):
        print("汪汪叫")

class XTQ(Dog): # 支持多层的继承
    pass

gou1 = XTQ()
gou1.bark()
gou1.eat()