tuple1 = (1,2,3) # 元组可拆包
str1 = 'bye' # 字符串可拆包
list1 = [1,2,3] # 列表可拆包
dict = {'a':1,"c":2,'d':4} # 字典也可以解包，赋值为key，但因无序，极少使用
m,n,k = dict
print(m,n,k)