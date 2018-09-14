# 可变类型： 允许在存储空间修改内容的
# 不可变类型： 无法在存储空间修改内容的
# 列表可变
a = [1,2,3]
print(id(a))
a.append(4)
print(id(a))

# 字典可变
a = {'a':1}
print(id(a))
a.update({'a':3})
print(id(a))

# 字符串不可变
# a = 'hello'
# print(id(a))
# b = a.replace('o','a')
# print(id(b))

# # 数字不可变,元组不可变
# a=11
# print(id(a))
# a=12
# print(id(a))

# 默认参数尽量不要使用可变类型
def func1(list1=[]):
    list1.append(2)
    print(list1)
func1() # 没有赋值，一直在引用第一次定义的默认空间位置
func1()
func1()
func1([1]) # 每次都赋值列表，申请了新的空间位置
func1([1])


# 试试不可变类型
def test(str1=" "):
    print(id(str1))
    str2 = str1 + "2"
    print(id(str2))
test()
test()
test('1')
