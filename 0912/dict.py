D = {'name'  :'yangjie',
     'name'  : 'lifangyue',
     'age'   :'30',
     'weight':'50',
     'height':"165cm"}
D['new_name'] = 'yangjie'
# del D['age']
# print(D)

# result = D.pop('age')
# print(result)

# result = D.pop('new_name') #key不存在默认会报错

""" result = D.pop('new_name','nokey')
if result == 'nokey':
        print("没有这个键")
else:
    print(D) """

# setdefault

""" print(D)
D.setdefault('new_name','chenyang') #已存在的键则不修改
print(D)
D.setdefault('old_name','chenyang') # 没有会添加
print(D) """

# update
print(D)
D.update({'name':'chenyang'})
print(D)

C=D.get('ne_name','lifangyue')
print(C)