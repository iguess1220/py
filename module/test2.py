# 可直接导入文件名，没后缀， 可使用函数和全局变量
# import test
# test.haha()
# print(test.Count)


# from test import haha,Count,Dog
# haha()
# print(Count)

from test import *  # 当导入* 或者直接import 文件名时，会先执行一遍该文件
haha()
#