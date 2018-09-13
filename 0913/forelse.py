a = [1,2,3,4,5]
for i in a: #如果列表中没有一个元素满足要求，执行else
    print('hehe')
    if i == 3:
        break
else: # 一般循环完成就执行else,除非循环中触发了break
    print('执行完执行else')