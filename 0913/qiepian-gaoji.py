a = 'hello,chenyang,nihbao a avdfg'
# 切片步长
# a[:] #从开始到结束
# a[::2] #步长为2 索引加2取值，默认为1
print(a[::-1]) # 步长可以为负数
print(a[::-2])  # 如果步长为负数，则倒着数，如果从最后一个开始，则可省略冒号前，如果到第一位结束，则省略冒号后，注意倒取第一位时，0位取不到，必须冒号

