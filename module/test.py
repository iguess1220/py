__all__ = ["Count",'haha']  # 当from xx import * 时 通配符选定的为__all__的内容

def haha():
    print("hello,world")
Count = 10

class Dog:
    pass


if __name__ == '__main__':
    """当__name__在所在自己文件中被访问时为__main__ ,当被作为模块导入其他文件时，在其他文件中为自己的文件名称"""
    print("测试")
    haha()