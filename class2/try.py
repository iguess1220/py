# with open('cy.txt','w') as f:
#     f.write("hello,world")

# try:
#     print(a)
# except Exception as error:  # exception 可捕获所有异常
#     print(error)


try:
    path = input("please input this file path: ")
    with open(path,'r') as f:
        print(f.read())
except FileNotFoundError as error:
    print("提示: 文件不存在, %s" %error)
except Exception as e:
    print(e)
else:
    print("没有捕获到异常的时候，执行else")
finally:
    print("不管是否捕获到异常，都要执行finally")

#
# try:
#     print(a)
# except NameError as e :
#     print(e)




print("程序结束")
