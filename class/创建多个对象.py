class Dog:
    def eat(self):
        print("吃东西")
dog1 = Dog()
dog1.eat()


dog2 = Dog()
dog2.eat()


print(dog1,dog2)
dog1.name = "旺财"
dog2.name = "来福"
print(dog1.name,dog2.name)
print(dog1.__doc__)