
# 在try嵌套中，如果在内部没有捕获到该异常，会想外层传递继续捕获，在函数内也是这样
try:
    with open('cy.txt') as f:
        try:
            content =f.read()
            print('****')
            print(a)
            print('!!!!!')
        except Exception as e :
            print(e)
            print(content)
except:
    print("异常")