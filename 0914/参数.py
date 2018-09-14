# 位置参数
def haha(num1,num2):
    return num1+num2
haha(1,2) 
#  形参和实参必须一一对应

# 默认参数
def hehe(num1,num2=10):
    return num1+num2
hehe(1)  # 给参数设定默认值，若传入则替代，不传入则为默认值，非默认参数必须在默认参数前面

# 管文里解释：  argument 为实参， paramenter 形参


# 关键字参数
# 给实参指定形参赋值
def hh(num1,num2):
    return num1+num2
#hh(num2=1,num1=3) # hh() got multiple values for argument 'num1'



# 可变参数
def all_sum(*args):
    # 可变参数会将任意数量的实参组成元组传递给形参
    result = 0
    for i in args:
        result += i
    return result
A_sum = all_sum(1,2,3,4,5)
print(A_sum)

        
