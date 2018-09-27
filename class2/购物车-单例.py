class shopingcart:
    __instance = None
    __has_init = False
    # 创建单例对象
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance
        # 单例模式下，初始化也需要做判断，保证只做一次初始化
    def __init__(self):
        if shopingcart.__has_init is False:
            self.total_price = 0
            shopingcart.__has_init = True

cart1 = shopingcart()
cart1.total_price = 200
print(cart1.total_price)
cart2 = shopingcart()
print(cart2.total_price)
