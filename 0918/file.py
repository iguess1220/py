# 基本的文件写入，不执行close()关闭文件会导致内存泄漏
# f = open("123.txt",'w')
# f.write("hello,world,hhahahaha")
# 不关闭导致内存泄漏，一些不再使用的数据保留在内存中，且无法回收
# f.close()

#方式2，可自动关闭，防止泄露 ,文件不存在会创建，有文件会替换，原文件丢失
# with open("C:/Users/17710/OneDrive/study/py/0918/123.txt",'w') as f: # 缩进执行完，自动关闭
#     f.write("hello,world")


# 'w'模式只能写入，不能读取
# with open("C:/Users/17710/OneDrive/study/py/0918/123.txt",'r',encoding='utf-8') as file:
#     context = file.read()
#     print(context)


# 'a'模式，追加写入，没有文件会新建

# with open("123.txt",'w') as f:
#     f.write("测试")
# with open("123.txt",'rb') as t:
#     content = t.read()
# print(content)

# read方法一次读取大文件会容易达到内存峰值
# 可指定读取的字符 read(n)
# with open("123.txt",'r') as target:
#     result = target.read(4)
# print(result)

# 一次读取一行
# with open("123.txt",'r') as target:
#     result = target.readline()
#     print(result,end="")
#     result1 = target.readline()
#     print(result1,end="")
# 读大型文件，开启循环，加入判断，最后位空字符串 ""，即len(result) == 0
""" with open("123.txt",'r') as target:
    while True :
        result = target.readline()
        if len(result) == 0 :
            break
        print(result,end="") """

# readlines 返回一个列表，每行内容是列表的一个元素
with open("123.txt",'r') as file:
    list1 = file.readlines()
    print(list1)





