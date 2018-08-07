L=[x*x for x in range(1,10)]
print(L)
g=(x*x for x in range(1,10))
#print(next(g))
#print(next(g))
'''
我们创建了一个generator后，基本上永远不会调用next()，而是通过for循环来迭代它，并且不需要关心StopIteration的错误
'''
for n in g:
    print(n)

'''
斐波拉契数列
'''

def fib(max):
    n,a,b=0,0,1
    while n < max:
        a,b=b,a+b
        n += 1
        print(a)
    return 'yueyue'
fib(10)

print('\n\n\n\n\n\nfib_g')

'''
generator 和函数的差别，在于yield ，函数顺序执行到最后一行或者return结束，而生成式是每次调用时执行next()，遇到yield返回。再次执行时从yield处继续执行
'''
def fib_g(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n += 1
    return 'yueyue'
g=fib_g(10)
print(next(g))
print(next(g))
print(next(g))

'''
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 2
    print('step 3')
    yield 3
a=odd()
next(a)
print(next(a))
'''


gg=fib_g(10)
while True:
    try:
        x=next(gg)
        print('gg:',x )
    except StopIteration as e:
        print('Generator return value: ',e.value)
        break









def triangles():
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [L[x - 1] + L[x] for x in range(len(L))]
t=triangles()
print(next(t))
print(next(t))
print(next(t))
print(next(t))
print(next(t))
print(next(t))
print(next(t))