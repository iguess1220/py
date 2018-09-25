class Dog:
    def __init__(self):
        print("现在执行初始化")
    def __del__(self): # 设置对象的“临终遗言”，可以检查某个对象是否删除
        print("现在删除对象")

# dog1 = Dog()
# del dog1
# print("*" * 10)

# “对象”的引用 被删除时会执行: 类内魔法方法 __del__ ,对象被赋值的话，会持续引用，
dog1 = Dog()

a = dog1

del dog1

print("*" * 20)
