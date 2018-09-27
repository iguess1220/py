# 自定义异常
class custemException(Exception):
    pass

try:
    num = input("请输入手机号码: ")
    if len(num) != 11:
            raise custemException("不足11位数")
except custemException as err:
    print("出现异常：%s" % err)