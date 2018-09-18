# 求4的阶乘 4*3*2*1
def fun1(num):
    result_num = 1
    i = 1
    while i <= num:
        result_num *= i
        i += 1
    return result_num
print(fun1(5))


def fun2(num):
    if num == 1:
        return num
    else:
        return num*fun2(num - 1)
print(fun2(5))