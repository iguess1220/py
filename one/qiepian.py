L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# 取前三个元素
print(L[:3])
# 取出第二个和第三个
print(L[1:3])
# 取倒数第一个
print(L[-1])
# 倒数第一个和第二个
print(L[-2:])
# 倒数第二个到倒数第一个，不含第一
print(L[-2:-1])
# 取0--100的前10个
print(list(range(100))[0:10])
# 分解上边的
L=list(range(100))
print(L[-10:])
# 11-20
print(L[11:21])
# 每两个取一次
print(L[0:10:2])
# 所有的每5个取一次
print(L[::5])
# 只一个冒号，全部输出
print(L[:])

print('\n\n\n\n\n')

#tuple也可以切片
t=(1,2,3,4,5)
print(t[1:4])
